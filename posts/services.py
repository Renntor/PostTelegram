import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
from django.conf import settings

if not settings.configured:
    django.setup()

import telebot
from dotenv import load_dotenv
from telebot import types
from users.models import User


load_dotenv()



def telegram_bot():
    tg_token = os.getenv("API_TELEGRAM_BOT")
    bot = telebot.TeleBot(tg_token)

    kb = types.InlineKeyboardMarkup(row_width=1)
    btn_post = types.InlineKeyboardButton(text='Сделать пост', callback_data='btn_post')
    kb.add(btn_post)
    btn_help = types.InlineKeyboardButton(text='help', callback_data='btn_help')
    kb.add(btn_help)

    @bot.message_handler(commands=['start'])
    def send_greeting(message: types.Message):
        user_id = message.from_user.id
        if bool(User.objects.filter(telegram_id=user_id)) is False:
            User.objects.create(
                telegram_id=user_id,
                telegram_name=message.from_user.username
            )
        bot.send_message(message.chat.id, f"""Добро пожаловать!\nЭтот бот предоставит вам
функционал для публикации постов в канал. Выберите функционал.""", reply_markup=kb)

    @bot.callback_query_handler(func=lambda call: True)
    def reactions(call):
        if call.data == 'btn_post':
            post_channel(call.message)

        elif call.data == 'btn_help':
            bot.send_message(call.message.chat.id, 'blah')

    @bot.channel_post_handler()
    def post_channel(message: types.Message):
        bot.send_message(os.getenv('CHANNEL'), 'test')


    # @bot.channel_post_handler(func=lambda call: True)
    # def post_channel(call):
    #     print(1)
    #     bot.send_message(call.message.chat.id, 'test')


    bot.polling()

telegram_bot()
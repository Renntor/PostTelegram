from users.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """
        Создания супер пользователя
        """
        user = User.objects.create(
            telegram_id='admin',
            telegram_name='1admin',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('admin')
        user.save()
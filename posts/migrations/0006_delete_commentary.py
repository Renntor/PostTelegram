# Generated by Django 5.0.4 on 2024-05-02 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_post_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Commentary',
        ),
    ]

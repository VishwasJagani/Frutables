# Generated by Django 5.1.3 on 2024-11-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_register_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quality',
        ),
        migrations.AlterField(
            model_name='register',
            name='token',
            field=models.IntegerField(default=7575),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_register_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='token',
            field=models.IntegerField(default=7689),
        ),
    ]

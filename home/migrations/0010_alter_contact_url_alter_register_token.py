# Generated by Django 5.1.3 on 2024-11-30 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_contact_alter_register_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='register',
            name='token',
            field=models.IntegerField(default=9093),
        ),
    ]

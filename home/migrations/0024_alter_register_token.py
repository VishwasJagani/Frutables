# Generated by Django 5.1.3 on 2024-12-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_subcategory_alter_register_token_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='token',
            field=models.IntegerField(default=3160),
        ),
    ]
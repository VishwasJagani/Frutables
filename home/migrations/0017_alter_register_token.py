# Generated by Django 5.1.3 on 2024-11-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_product_quilty_remove_product_subcat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='token',
            field=models.IntegerField(default=9578),
        ),
    ]

# Generated by Django 3.2.12 on 2022-07-16 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0007_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, default='', null=True, unique=True),
        ),
    ]

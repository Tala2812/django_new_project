# Generated by Django 5.1.7 on 2025-03-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newspost',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='newspost',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Автор новости'),
        ),
    ]

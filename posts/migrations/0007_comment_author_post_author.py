# Generated by Django 4.0.4 on 2022-05-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='None', max_length=50, verbose_name='Логин автора'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='None', max_length=50, verbose_name='Логин автора'),
        ),
    ]

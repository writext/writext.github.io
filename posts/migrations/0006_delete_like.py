# Generated by Django 4.0.4 on 2022-05-18 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_comment_pub_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]

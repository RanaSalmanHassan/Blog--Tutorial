# Generated by Django 4.1.1 on 2023-03-20 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

# Generated by Django 3.2 on 2021-04-24 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0011_alter_cake_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cake',
        ),
        migrations.DeleteModel(
            name='Imagemodel',
        ),
    ]

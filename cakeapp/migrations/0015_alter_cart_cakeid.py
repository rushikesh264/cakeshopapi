# Generated by Django 3.2 on 2021-04-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0014_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cakeid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
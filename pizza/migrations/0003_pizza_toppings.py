# Generated by Django 3.0 on 2020-11-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_pizza'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='pizza.Toppings'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkapp', '0009_auto_20211210_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='no_of_slots',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
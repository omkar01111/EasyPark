# Generated by Django 3.2.8 on 2021-11-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkapp', '0005_remove_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkapp', '0008_book_bool_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='spot',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='bool_value',
            field=models.BooleanField(default=False),
        ),
    ]

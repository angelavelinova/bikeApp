# Generated by Django 2.0.7 on 2019-06-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_auto_20190602_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='model',
            new_name='current_owner',
        ),
        migrations.AddField(
            model_name='bike',
            name='reserved',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
    ]

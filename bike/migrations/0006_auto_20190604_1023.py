# Generated by Django 2.0.7 on 2019-06-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0005_auto_20190604_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='reservator',
            field=models.CharField(default='None', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='bike',
            name='current_owner',
            field=models.CharField(default='None', max_length=256, null=True),
        ),
    ]

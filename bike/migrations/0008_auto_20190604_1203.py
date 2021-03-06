# Generated by Django 2.0.7 on 2019-06-04 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bike', '0007_auto_20190604_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='bike',
            name='bike_id',
        ),
        migrations.AddField(
            model_name='bikereservation',
            name='bike_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.Bike'),
        ),
        migrations.AddField(
            model_name='bikereservation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

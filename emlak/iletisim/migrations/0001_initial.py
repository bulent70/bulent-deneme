# Generated by Django 3.2.2 on 2021-05-23 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iletisim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilan', models.CharField(max_length=200)),
                ('ilan_id', models.IntegerField()),
                ('isim', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('telefon', models.CharField(max_length=100)),
                ('mesaj', models.TextField(blank=True)),
                ('iletisim_tarihi', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('kullanici_id', models.IntegerField(blank=True)),
            ],
        ),
    ]

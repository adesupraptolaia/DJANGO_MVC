# Generated by Django 2.2.3 on 2019-07-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kebun_Binatang', '0002_auto_20190722_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjaga',
            name='jadwal_jaga',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-24 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_mentee'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=255)),
                ('tanggal', models.DateField()),
                ('banyakkomen', models.CharField(max_length=255)),
                ('judul', models.CharField(max_length=255)),
                ('isi', models.TextField()),
            ],
        ),
    ]

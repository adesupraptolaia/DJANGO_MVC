# Generated by Django 2.2.3 on 2019-07-23 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='foto',
            field=models.CharField(default='a', max_length=255),
        ),
    ]

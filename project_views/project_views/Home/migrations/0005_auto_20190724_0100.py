# Generated by Django 2.2.3 on 2019-07-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='foto',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='foto',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-22 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATA', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='challenge',
            options={'verbose_name': 'Challenge', 'verbose_name_plural': 'Challenge'},
        ),
        migrations.AlterModelOptions(
            name='direksi',
            options={'verbose_name': 'Direksi', 'verbose_name_plural': 'Direksi'},
        ),
        migrations.AlterModelOptions(
            name='live_code',
            options={'verbose_name': 'Live Code', 'verbose_name_plural': 'Live Code'},
        ),
        migrations.AlterModelOptions(
            name='mata_pelajaran',
            options={'verbose_name': 'Mata Pelajaran', 'verbose_name_plural': 'Mata Pelajaran'},
        ),
        migrations.AlterModelOptions(
            name='mentee',
            options={'verbose_name': 'Mentee', 'verbose_name_plural': 'Mentee'},
        ),
        migrations.AlterModelOptions(
            name='mentor',
            options={'verbose_name': 'Mentor', 'verbose_name_plural': 'Mentor'},
        ),
    ]
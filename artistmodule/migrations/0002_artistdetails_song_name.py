# Generated by Django 4.2.6 on 2024-03-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistmodule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistdetails',
            name='song_name',
            field=models.CharField(default='Default Song Name', max_length=100),
        ),
    ]
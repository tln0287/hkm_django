# Generated by Django 4.0 on 2022-01-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='about_image',
            field=models.ImageField(null=True, upload_to='about/'),
        ),
    ]
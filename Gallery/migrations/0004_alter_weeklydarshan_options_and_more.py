# Generated by Django 4.0 on 2022-01-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0003_weeklydarshan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weeklydarshan',
            options={'verbose_name_plural': 'Weekly Darshan'},
        ),
        migrations.AlterField(
            model_name='weeklydarshan',
            name='gallery_image',
            field=models.ImageField(upload_to='weekly darshan/'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0007_alter_videos_youtube_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festivaldarshan',
            name='gallery_image',
            field=models.ImageField(upload_to='festivaldarshan/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='gallery_image',
            field=models.ImageField(upload_to='gallerymedia/'),
        ),
        migrations.AlterField(
            model_name='weeklydarshan',
            name='gallery_image',
            field=models.ImageField(upload_to='weeklydarshan/'),
        ),
    ]

# Generated by Django 4.0 on 2022-01-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0004_alter_weeklydarshan_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FestivalDarshan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('gallery_image', models.ImageField(upload_to='festival darshan/')),
            ],
            options={
                'verbose_name_plural': 'Festival Darshan',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('gallery_image', models.ImageField(upload_to='gallery media/')),
            ],
            options={
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('youtube_links', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Videos',
            },
        ),
    ]

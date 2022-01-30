# Generated by Django 3.2.7 on 2022-01-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0002_aboutus_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('designation', models.CharField(blank=True, max_length=500, null=True)),
                ('photo', models.ImageField(null=True, upload_to='team/')),
                ('facebook', models.CharField(blank=True, max_length=500, null=True)),
                ('instagram', models.CharField(blank=True, max_length=500, null=True)),
                ('youtubechannel', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Team',
            },
        ),
    ]

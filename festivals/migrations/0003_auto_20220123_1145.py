# Generated by Django 3.2.7 on 2022-01-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0002_festivals_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='festivals',
            name='fest_image1',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AddField(
            model_name='festivals',
            name='fest_image10',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AddField(
            model_name='festivals',
            name='fest_image2',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AddField(
            model_name='festivals',
            name='fest_image3',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AddField(
            model_name='festivals',
            name='fest_image4',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AddField(
            model_name='festivals',
            name='fest_image5',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AddField(
            model_name='festivals',
            name='fest_image6',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AddField(
            model_name='festivals',
            name='fest_image7',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AddField(
            model_name='festivals',
            name='fest_image8',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AddField(
            model_name='festivals',
            name='fest_image9',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AlterField(
            model_name='festivals',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
    ]

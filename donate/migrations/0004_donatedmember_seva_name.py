# Generated by Django 4.0 on 2022-01-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0003_donatedmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatedmember',
            name='seva_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

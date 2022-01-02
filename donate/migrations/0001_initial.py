# Generated by Django 4.0 on 2022-01-02 06:05

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('donation_title', models.CharField(blank=True, max_length=500, null=True)),
                ('donation_required_amount', models.IntegerField(null=True)),
                ('donation_raised', models.IntegerField(null=True)),
                ('content', tinymce.models.HTMLField(default='<p>Add content</p>')),
            ],
            options={
                'verbose_name_plural': 'Donations',
            },
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Component', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='image',
            field=models.ImageField(blank=True, default='null', max_length='300', null=True, upload_to='images/'),
        ),
    ]

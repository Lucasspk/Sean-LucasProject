# Generated by Django 5.0.6 on 2024-06-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Component', '0002_component_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='yearReleased',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='gpu',
            name='fpsrt1080',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='gpu',
            name='fpsrt1440',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='gpu',
            name='fpsrt4k',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='gpu',
            name='gpuClock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gpu',
            name='memory',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_clubs', '0005_alter_club_award_silver_alter_horsebreed_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='award_silver',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='horsebreed',
            name='breed',
            field=models.CharField(choices=[('Friesian', 'Friesian'), ('Andalusian', 'Andalusian'), ('Arabian', 'Arabian')], max_length=35),
        ),
    ]

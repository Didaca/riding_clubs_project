# Generated by Django 4.0.3 on 2022-04-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_clubs', '0002_club_award_bronze_club_award_gold_club_award_silver_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'ordering': ('award_gold', 'award_silver', 'award_bronze')},
        ),
        migrations.AlterField(
            model_name='horsebreed',
            name='breed',
            field=models.CharField(choices=[('Arabian', 'Arabian'), ('Andalusian', 'Andalusian'), ('Friesian', 'Friesian')], max_length=35),
        ),
    ]

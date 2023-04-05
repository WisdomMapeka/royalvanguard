# Generated by Django 4.1.7 on 2023-04-03 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_aboutus_image_secttion1_aboutus_image_secttion2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='image_secttion2',
            new_name='image_our_beliefs',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='secttion2',
        ),
        migrations.AddField(
            model_name='ourbeliefs',
            name='belief_type',
            field=models.CharField(blank=True, choices=[('values', 'values'), ('belied', 'belief')], max_length=100, null=True),
        ),
    ]
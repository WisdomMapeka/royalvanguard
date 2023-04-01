# Generated by Django 4.1.7 on 2023-04-01 12:11

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_remove_summaryservices_background_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=tinymce.models.HTMLField(blank=True, help_text='Information added here, will be displayed on the about page, put as much as you can, eg history, values, mission and more', null=True),
        ),
    ]
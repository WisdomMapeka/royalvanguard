# Generated by Django 4.1.7 on 2023-04-03 18:44

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_aboutus_summary2_aboutus_title2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='image',
            new_name='image2',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image_homepage',
            field=models.ImageField(blank=True, null=True, upload_to='AboutUsImages/'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image_main',
            field=models.ImageField(blank=True, null=True, upload_to='AboutUsImages/'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='summary_homepage',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_homepage',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

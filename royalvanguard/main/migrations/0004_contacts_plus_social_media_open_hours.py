# Generated by Django 4.1.7 on 2023-03-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contacts_plus_social_media_facebook_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts_plus_social_media',
            name='open_hours',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

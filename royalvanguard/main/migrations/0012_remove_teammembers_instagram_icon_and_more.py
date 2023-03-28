# Generated by Django 4.1.7 on 2023-03-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_delete_freequote_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammembers',
            name='instagram_icon',
        ),
        migrations.RemoveField(
            model_name='teammembers',
            name='linkedin_icon',
        ),
        migrations.RemoveField(
            model_name='teammembers',
            name='twitter_icon',
        ),
        migrations.AddField(
            model_name='teammembers',
            name='instagram_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammembers',
            name='linkedin_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammembers',
            name='twitter_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]

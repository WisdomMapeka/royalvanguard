# Generated by Django 4.1.7 on 2023-03-30 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_aboutus_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammembers',
            old_name='linkedin_link',
            new_name='facebook_link',
        ),
    ]

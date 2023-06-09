# Generated by Django 4.1.7 on 2023-04-02 20:59

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_backgroundimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sectors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('summary', models.CharField(blank=True, max_length=500, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('incon', models.ImageField(blank=True, help_text="This is a small image which represents information added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>", null=True, upload_to='Services/', verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Sectors [max 6]',
                'verbose_name_plural': 'Sectors [max 6]',
            },
        ),
        migrations.AlterModelOptions(
            name='whychooseus',
            options={'verbose_name': 'Coming Soon', 'verbose_name_plural': 'Coming Soon'},
        ),
        migrations.AlterModelOptions(
            name='whychooseussummary',
            options={'verbose_name': 'Coming Soon Brief Information', 'verbose_name_plural': 'Coming Soon Brief Information'},
        ),
        migrations.AlterField(
            model_name='whychooseus',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]

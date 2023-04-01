# Generated by Django 4.1.7 on 2023-04-01 12:04

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_delete_newsletter_delete_shophomepagelabels_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summaryservices',
            name='background_image',
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='incon',
            field=models.ImageField(blank=True, help_text="This is a small image which represents information added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>", null=True, upload_to='AboutUsImages/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='incon2',
            field=models.ImageField(blank=True, help_text="This is a small image which represents information added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>", null=True, upload_to='AboutUsImages/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='incon_explanation',
            field=models.CharField(blank=True, default='4', max_length=200, null=True, verbose_name='Number Of Clients'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='incon_explanation2',
            field=models.CharField(blank=True, default='12', max_length=200, null=True, verbose_name='NUmber Of Projects'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='incon_second_explanation',
            field=models.CharField(blank=True, default='Clients', help_text='Title can be Clients or Any Other Word', max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='incon_second_explanation2',
            field=models.CharField(blank=True, default='Projects', help_text='Title can be Projects or Any Other Word', max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='contacts_plus_social_media',
            name='opening_message',
            field=tinymce.models.HTMLField(blank=True, help_text='Information added on this field will be displayed at the top of the contact page', null=True, verbose_name='About Us Page Introduction Text'),
        ),
        migrations.AlterField(
            model_name='services',
            name='incon',
            field=models.ImageField(blank=True, help_text="This is a small image which represents information added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>", null=True, upload_to='Services/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='summaryservices',
            name='incon',
            field=models.ImageField(blank=True, help_text="This is a small image which represents a service added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>", null=True, upload_to='SummaryServices/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='whychooseus',
            name='incon',
            field=models.ImageField(blank=True, help_text="This is a small image which represents information added, you can download more from this webiste <a href='https://www.flaticon.com/' target='_blank' rel='noopener noreferrer'>Click To Download Icons</a>", null=True, upload_to='WhyChooseUs/', verbose_name='Icon'),
        ),
    ]

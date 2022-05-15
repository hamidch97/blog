# Generated by Django 4.0.4 on 2022-05-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_profil'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='profil_pic',
            field=models.ImageField(blank=True, null=True, upload_to='img/profile'),
        ),
        migrations.AddField(
            model_name='profil',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

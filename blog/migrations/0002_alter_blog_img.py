# Generated by Django 4.0.2 on 2022-02-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
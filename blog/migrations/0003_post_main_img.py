# Generated by Django 5.1.4 on 2025-01-20 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Main_Img',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]

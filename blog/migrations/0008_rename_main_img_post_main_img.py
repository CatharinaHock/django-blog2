# Generated by Django 5.1.4 on 2025-01-21 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_brief_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Main_Img',
            new_name='main_img',
        ),
    ]
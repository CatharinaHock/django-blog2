# Generated by Django 5.1.4 on 2025-02-05 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_color_tag_text_color_tag_background_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_warning',
            field=models.TextField(blank=True),
        ),
    ]

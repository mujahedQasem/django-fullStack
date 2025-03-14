# Generated by Django 5.1.6 on 2025-03-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tv_show',
            name='release_date',
            field=models.DateTimeField(null='null'),
            preserve_default='null',
        ),
        migrations.AlterField(
            model_name='tv_show',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tv_show',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-25 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_community_app', '0007_dogs_dog_image_alter_team_member_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breed',
            name='breed_article',
        ),
        migrations.AddField(
            model_name='breed',
            name='bred_for',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='breed',
            name='life_span',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='breed',
            name='origin',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='breed',
            name='temperament',
            field=models.CharField(default='', max_length=1000),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='like count'),
        ),
    ]

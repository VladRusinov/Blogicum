# Generated by Django 3.2.16 on 2023-07-02 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_count',
            field=models.IntegerField(default=0, verbose_name='колличество комментариев'),
        ),
    ]

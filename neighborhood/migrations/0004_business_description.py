# Generated by Django 2.0 on 2018-11-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0003_auto_20181123_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]

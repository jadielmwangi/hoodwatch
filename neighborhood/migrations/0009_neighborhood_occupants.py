# Generated by Django 2.0 on 2018-11-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0008_auto_20181125_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='occupants',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 2.0 on 2018-11-25 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood', '0007_auto_20181125_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighborhood.Category'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighborhood.Location'),
        ),
    ]

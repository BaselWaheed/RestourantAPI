# Generated by Django 3.2.10 on 2022-03-27 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_verify',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]

# Generated by Django 3.2.10 on 2022-05-12 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_auto_20220501_0454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='birthdata',
            new_name='birthdate',
        ),
    ]

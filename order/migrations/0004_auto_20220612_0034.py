# Generated by Django 3.2.10 on 2022-06-11 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20220501_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_online',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20181024_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='alamat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='no_hape',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]

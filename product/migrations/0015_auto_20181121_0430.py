# Generated by Django 2.1.2 on 2018-11-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20181102_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalbelanja',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=15),
        ),
    ]
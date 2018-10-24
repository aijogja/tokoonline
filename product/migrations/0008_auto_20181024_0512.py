# Generated by Django 2.1.2 on 2018-10-24 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20181015_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('cart', 'In Cart'), ('checkout', 'Checkout'), ('paid', 'Terbayar'), ('delivered', 'Terkirim')], default='cart', max_length=10),
        ),
    ]

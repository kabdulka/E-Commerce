# Generated by Django 3.2.12 on 2022-05-09 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auto_20220509_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_bid', to='auctions.bid'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='currentBid',
            field=models.FloatField(blank=True, default=0.01),
        ),
    ]

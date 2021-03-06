# Generated by Django 3.2.12 on 2022-05-09 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20220506_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='bid',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bidOwner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listing',
            name='bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_bid', to='auctions.bid'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='startingBid',
            field=models.FloatField(blank=True, default=0),
        ),
    ]

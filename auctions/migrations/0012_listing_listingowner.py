# Generated by Django 3.2.12 on 2022-05-04 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_listing_startingbid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listingOwner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='myListing', to=settings.AUTH_USER_MODEL),
        ),
    ]

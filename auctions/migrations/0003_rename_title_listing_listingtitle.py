# Generated by Django 3.2.12 on 2022-04-29 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='title',
            new_name='listingTitle',
        ),
    ]
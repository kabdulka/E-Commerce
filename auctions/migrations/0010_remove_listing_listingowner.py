# Generated by Django 3.2.12 on 2022-05-04 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20220504_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='listingOwner',
        ),
    ]
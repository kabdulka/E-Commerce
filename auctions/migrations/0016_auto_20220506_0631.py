# Generated by Django 3.2.12 on 2022-05-06 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20220505_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryText', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_listing', to='auctions.category'),
        ),
    ]
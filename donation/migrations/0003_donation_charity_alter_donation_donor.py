# Generated by Django 5.0.4 on 2024-04-25 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0002_alter_charity_logo'),
        ('donation', '0002_donation_donor'),
        ('donor', '0002_alter_donor_options_alter_donor_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='charity',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='charity.charity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donations', to='donor.donor'),
        ),
    ]
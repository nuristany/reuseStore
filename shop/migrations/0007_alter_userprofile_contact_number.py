# Generated by Django 5.0.3 on 2024-03-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_item_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='contact_number',
            field=models.CharField(max_length=20),
        ),
    ]

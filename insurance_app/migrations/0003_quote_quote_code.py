# Generated by Django 5.0.6 on 2024-07-04 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0002_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='quote_code',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

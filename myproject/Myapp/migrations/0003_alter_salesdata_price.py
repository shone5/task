# Generated by Django 4.1.2 on 2023-03-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_remove_salesdata_image_salesdata_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.2 on 2023-03-22 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0005_alter_salesdata_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
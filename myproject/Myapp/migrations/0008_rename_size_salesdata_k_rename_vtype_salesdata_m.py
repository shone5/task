# Generated by Django 4.1.2 on 2023-03-25 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0007_salesdata_orderno_salesdata_size_salesdata_vtype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesdata',
            old_name='size',
            new_name='K',
        ),
        migrations.RenameField(
            model_name='salesdata',
            old_name='vtype',
            new_name='M',
        ),
    ]

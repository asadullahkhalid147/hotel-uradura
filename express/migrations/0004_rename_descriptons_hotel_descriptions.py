# Generated by Django 5.0.1 on 2024-03-05 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0003_remove_hotel_hotel_img2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='descriptons',
            new_name='descriptions',
        ),
    ]

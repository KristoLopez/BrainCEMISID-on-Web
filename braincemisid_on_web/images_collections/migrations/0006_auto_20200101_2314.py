# Generated by Django 2.2.7 on 2020-01-02 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images_collections', '0005_auto_20200101_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagesfromneuron',
            old_name='image',
            new_name='img',
        ),
    ]
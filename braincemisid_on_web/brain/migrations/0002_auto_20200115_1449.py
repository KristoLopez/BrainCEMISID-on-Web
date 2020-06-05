# Generated by Django 3.0.2 on 2020-01-15 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snb_h',
            name='brain_h',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain'),
        ),
        migrations.AlterField(
            model_name='snb_s',
            name='brain_s',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brain.brain'),
        ),
    ]
# Generated by Django 5.1.4 on 2025-01-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0002_alter_items_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Item_name',
            field=models.CharField(max_length=40),
        ),
    ]
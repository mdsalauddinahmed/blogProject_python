# Generated by Django 4.2.9 on 2024-02-14 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category',
            new_name='name',
        ),
    ]
# Generated by Django 3.0.5 on 2020-10-28 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pleethai', '0007_auto_20200804_1640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['id']},
        ),
    ]
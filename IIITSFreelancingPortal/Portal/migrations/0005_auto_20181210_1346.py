# Generated by Django 2.1.1 on 2018-12-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0004_auto_20181208_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_link',
            field=models.URLField(blank=True),
        ),
    ]

# Generated by Django 2.1.7 on 2022-10-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0005_auto_20181210_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], default='Student', max_length=10),
        ),
    ]

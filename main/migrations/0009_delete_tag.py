# Generated by Django 4.0.4 on 2022-06-07 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_course_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]

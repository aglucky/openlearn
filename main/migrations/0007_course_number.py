# Generated by Django 4.0.4 on 2022-06-07 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]

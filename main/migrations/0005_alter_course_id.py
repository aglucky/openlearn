# Generated by Django 4.0.4 on 2022-06-06 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
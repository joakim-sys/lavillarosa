# Generated by Django 5.0.6 on 2024-08-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_service_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(default='bi-house', max_length=255, null=True),
        ),
    ]

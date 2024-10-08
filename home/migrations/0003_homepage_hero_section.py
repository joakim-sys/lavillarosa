# Generated by Django 5.0.6 on 2024-07-29 11:45

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_section',
            field=wagtail.fields.StreamField([('carousel', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.TextBlock(required=False)), ('page', wagtail.blocks.PageChooserBlock(required=False))]))], blank=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-29 13:29

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_service_service_page_alter_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='gallery',
            field=wagtail.fields.StreamField([('gallery', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.RichTextBlock(required=False))]))], blank=True, help_text='Add high-quality images to showcase the hotel.'),
        ),
    ]

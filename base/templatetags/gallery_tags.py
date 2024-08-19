from django import template
from wagtail.images.models import Image

register = template.Library()


# Retrieves a single gallery item and returns a gallery of images
@register.simple_tag(takes_context=True)
def gallery(context, gallery):
    images = Image.objects.filter(collection=gallery)
    return images
from wagtail.blocks import StructBlock, CharBlock, PageChooserBlock, TextBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock


class CarouselBlock(StructBlock):
    heading = CharBlock()
    paragraph = TextBlock(required=False)

    page = PageChooserBlock(required=False)
    image = ImageChooserBlock()

    # class Meta:
    #     template = 'blocks/carousel_block.html'

class AboutSectionBlock(StructBlock):
    heading = CharBlock()
    subheading = CharBlock(required=False)
    text = RichTextBlock(required=False)

class GalleryBlock(StructBlock):
    image = ImageChooserBlock()
    heading = CharBlock(required=False)
    description = RichTextBlock(required=False)

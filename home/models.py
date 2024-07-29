from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from modelcluster.models import ClusterableModel, ParentalKey
from .blocks import CarouselBlock, AboutSectionBlock, GalleryBlock


class HomePage(Page):
    hero_section = StreamField(
        [("carousel", CarouselBlock())], blank=True, use_json_field=True
    )

    about_section = StreamField(
        [("about_body", AboutSectionBlock())], blank=True, use_json_field=True
    )
    gallery = StreamField(
        [("gallery", GalleryBlock())],
        blank=True,
        use_json_field=True,
        help_text="Add high-quality images to showcase the hotel.",
    )

    tabs_section_heading = models.CharField(null=True, blank=True, max_length=255)
    tabs_section_subheading = models.CharField(null=True, blank=True, max_length=255)

    about_section_heading = models.CharField(null=True, blank=True, max_length=255)
    about_section_subheading = models.CharField(null=True, blank=True, max_length=255)

    gallery_section_heading = models.CharField(null=True, blank=True, max_length=255)
    gallery_section_subheading = models.CharField(null=True, blank=True, max_length=255)

    services_section_heading = models.CharField(null=True, blank=True, max_length=255)
    services_section_subheading = models.CharField(
        null=True, blank=True, max_length=255
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_section"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    children=(
                        FieldPanel("about_section_heading"),
                        FieldPanel("about_section_subheading"),
                    ),
                    heading="Section Title",
                ),
                FieldPanel("about_section"),
            ],
            "About Section",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    children=(
                        FieldPanel("services_section_heading"),
                        FieldPanel("services_section_subheading"),
                    ),
                    heading="Section Title",
                ),
                InlinePanel("services", label="Services"),
            ],
            heading="Icon List Section",
            help_text="This section displays an icon, a heading and text",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    children=(
                        FieldPanel("gallery_section_heading"),
                        FieldPanel("gallery_section_subheading"),
                    ),
                    heading="Section Title",
                ),
                FieldPanel("gallery"),
            ],
            "Gallery Section",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    children=(
                        FieldPanel("tabs_section_heading"),
                        FieldPanel("tabs_section_subheading"),
                    ),
                    heading="Section Title",
                ),
                InlinePanel("tabs", label="Tabs"),
            ],
            "Tabs Section",
        ),
    ]

    def get_services(self):
        return [n.service for n in self.services.select_related("service")]

    def get_tabs(self):
        return [n.tab for n in self.tabs.select_related("tab")]


class Service(ClusterableModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    service_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page for this service",
    )

    icon = models.CharField(max_length=255, null=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("icon"),
        FieldPanel("service_page"),
    ]

    class Meta:
        verbose_name_plural = 'Icon Items'
        verbose_name = 'Icon Item'

    def __str__(self):
        return self.name


class ServiceOrderable(Orderable):
    page = ParentalKey("HomePage", related_name="services")
    service = models.ForeignKey("Service", on_delete=models.CASCADE)

    panels = [FieldPanel("service")]


class FeatureTab(ClusterableModel):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    def __str__(self):
        return self.title
    

class FeatureTabOrderable(Orderable):
    page = ParentalKey("HomePage", related_name="tabs")
    tab = models.ForeignKey("FeatureTab", on_delete=models.CASCADE)

    panels = [
        FieldPanel("tab"),
    ]

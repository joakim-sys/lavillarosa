from django.db import models
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, InlinePanel, FieldRowPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey


class StandardPage(Page):

    introduction = models.TextField(help_text="Text to describe the page", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("body"),
        FieldPanel("image"),
    ]


class FormField(AbstractFormField):
    page = ParentalKey("FormPage", related_name="form_fields", on_delete=models.CASCADE)


class FormPage(AbstractEmailForm):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("image"),
        FieldPanel("body"),
        InlinePanel("form_fields", heading="Form fields", label="Field"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address"),
                        FieldPanel("to_address"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]


@register_setting
class GenericSettings(ClusterableModel, BaseGenericSetting):
    x_url = models.URLField(verbose_name="X URL", blank=True)
    facebook_url = models.URLField(verbose_name="facebook URL", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    skype_url = models.URLField(verbose_name="Skype URL", blank=True)

    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel("phone"),
        FieldPanel("email"),
        FieldPanel("address"),
        MultiFieldPanel(
            [
                FieldPanel("x_url"),
                FieldPanel("facebook_url"),
                FieldPanel("instagram_url"),
                FieldPanel("linkedin_url"),
                FieldPanel("skype_url"),
            ],
            "Social Settings",
        ),
    ]

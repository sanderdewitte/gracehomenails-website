from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    hero_tagline = models.CharField(
        max_length=255,
        blank=True,
        default="Beautiful, carefully styled nails — from the comfort of a cosy home studio.",
    )
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Recommended: a wide photo, at least 1600px, of the salon or nail work.",
    )
    booking_url = models.URLField(
        blank=True,
        default="https://www.treatwell.nl/en/place/grace-home-nails/",
        help_text="Link to your booking tool, e.g. your Treatwell page",
    )
    booking_label = models.CharField(max_length=50, blank=True, default="Book Now")
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_tagline"),
        FieldPanel("hero_image"),
        FieldPanel("booking_url"),
        FieldPanel("booking_label"),
        FieldPanel("intro"),
    ]

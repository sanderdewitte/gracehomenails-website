from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from services.blocks import ServiceCategoryBlock


class ServicesPage(Page):
    intro = RichTextField(blank=True)
    body = StreamField(
        [("service_category", ServiceCategoryBlock())],
        blank=True,
        use_json_field=True,
    )
    booking_url = models.URLField(
        blank=True,
        help_text="Link to your booking tool, e.g. your Treatwell page",
    )
    booking_label = models.CharField(
        max_length=50, blank=True, default="Book Now"
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("booking_url"),
        FieldPanel("booking_label"),
    ]

    # Adjust "home.HomePage" if your actual home page model differs.
    parent_page_types = ["home.HomePage"]
    subpage_types = []

    class Meta:
        verbose_name = "Services Page"

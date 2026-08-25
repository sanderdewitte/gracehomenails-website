from wagtail import blocks


class ServiceItemBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=100)
    description = blocks.TextBlock(required=False)
    price = blocks.CharBlock(
        max_length=50,
        help_text="e.g. '€25' or 'from €9,50'",
    )
    duration = blocks.CharBlock(
        max_length=30,
        required=False,
        help_text="e.g. '45 mins' or '1 hr 15 mins'",
    )
    badge = blocks.CharBlock(
        max_length=50,
        required=False,
        help_text="Optional badge, e.g. 'Off peak' or 'Save up to 5%'",
    )

    class Meta:
        icon = "pick"


class ServiceCategoryBlock(blocks.StructBlock):
    category_name = blocks.CharBlock(max_length=100)
    services = blocks.ListBlock(ServiceItemBlock())

    class Meta:
        icon = "list-ul"

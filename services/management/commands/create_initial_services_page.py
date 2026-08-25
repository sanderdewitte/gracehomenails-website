from django.core.management.base import BaseCommand

from home.models import HomePage
from services.models import ServicesPage


class Command(BaseCommand):
    help = "Create the initial Services page if it does not already exist."

    def handle(self, *args, **options):

        home_page = HomePage.objects.filter(depth=2).first()

        if home_page is None:
            self.stdout.write(self.style.WARNING( "  No HomePage exists; skipping initial Services page creation."))
            return

        if ServicesPage.objects.child_of(home_page).filter(slug="services").exists():
            self.stdout.write("  Initial Services page already exists.")
            return

        page = ServicesPage(
            title="Services",
            slug="services",
            intro=(
                "<p>Explore our nail treatments below. "
                "All appointments are by booking only, "
                "at our cosy home studio.</p>"
            ),
            body=[
                {
                    "type": "service_category",
                    "value": {
                        "category_name": "Manicure",
                        "services": [
                            {
                                "name": "Manicure",
                                "description": "",
                                "price": "€25",
                                "duration": "45 mins",
                                "badge": "",
                            },
                            {
                                "name": "Russian Manicure",
                                "description": "",
                                "price": "€30",
                                "duration": "45 mins",
                                "badge": "",
                            },
                            {
                                "name": "Nail Repair",
                                "description": "",
                                "price": "from €4,75",
                                "duration": "15 mins",
                                "badge": "Save up to 5%",
                            },
                        ],
                    },
                },
                {
                    "type": "service_category",
                    "value": {
                        "category_name": "Gellak & BIAB",
                        "services": [
                            {
                                "name": "Manicure - Gellak",
                                "description": "",
                                "price": "from €38",
                                "duration": "1 hr 15 mins",
                                "badge": "Save up to 5%",
                            },
                            {
                                "name": "Gellak/BIAB removal",
                                "description": "",
                                "price": "€15",
                                "duration": "25 mins",
                                "badge": "",
                            },
                        ],
                    },
                },
                {
                    "type": "service_category",
                    "value": {
                        "category_name": "Nail Extensions",
                        "services": [
                            {
                                "name": "Nail Extensions - Removal",
                                "description": "",
                                "price": "from €19",
                                "duration": "30 mins",
                                "badge": "Save up to 5%",
                            },
                        ],
                    },
                },
                {
                    "type": "service_category",
                    "value": {
                        "category_name": "Specials",
                        "services": [
                            {
                                "name": "Chrome / Cat Eye / Special Effects (10 nails)",
                                "description": "",
                                "price": "from €9,50",
                                "duration": "30 mins",
                                "badge": "Save up to 5%",
                            },
                            {
                                "name": "French Tip (10 nails)",
                                "description": "",
                                "price": "from €14,25",
                                "duration": "30 mins",
                                "badge": "Save up to 5%",
                            },
                        ],
                    },
                },
            ],
            booking_url="https://www.treatwell.nl/en/place/grace-home-nails/",
            booking_label="Book Now",
        )

        home_page.add_child(instance=page)
        page.save_revision().publish()

        self.stdout.write(self.style.SUCCESS("  Initial Services page created."))

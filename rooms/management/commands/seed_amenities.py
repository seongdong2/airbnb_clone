from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates amenities"

    """
    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="몇 번을 사랑한다고 말해주면 좋겠니?",
        )
    """

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Heating",
            "Washer",
            "Wifi",
            "Indoor fireplace",
            "Iron",
            "Laptop friendly workspace",
            "Crib",
            "Self check-in",
            "Carbon monoxide detector",
            "Shampoo",
            "Air conditioning",
            "Dryer",
            "Breakfast",
            "Hangers",
            "Hair dryer",
            "TV",
            "High chair",
            "Smoke detector",
            "Private bathroom",
        ]

        for a in amenities:

            room_models.Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities Created!"))

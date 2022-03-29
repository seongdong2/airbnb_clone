from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates facilities"

    """def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="몇 번을 사랑한다고 말해주면 좋겠니?",
        )"""

    def handle(self, *args, **options):
        facilites = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for f in facilites:

            room_models.Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilites)} facilities Created!"))

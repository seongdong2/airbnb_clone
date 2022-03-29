import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="몇 개의 방을 만들면 좋겠니?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(0, 10),
                "price": lambda x: random.randint(0, 300),
                "beds": lambda x: random.randint(0, 3),
                "bedrooms": lambda x: random.randint(0, 4),
                "baths": lambda x: random.randint(0, 2),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities_foreignkey = room_models.Amenity.objects.all()
        facilities_foreignkey = room_models.Facility.objects.all()
        rules_foreignkey = room_models.HouseRule.objects.all()
        for pk in created_clean:
            room_foreignkey = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room_foreignkey,
                    file=f"/room_photos/{random.randint(1,31)}.webp",
                )
            for a in amenities_foreignkey:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_foreignkey.amenities.add(a)
            for f in facilities_foreignkey:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_foreignkey.facilities.add(f)
            for r in rules_foreignkey:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_foreignkey.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms Created!"))

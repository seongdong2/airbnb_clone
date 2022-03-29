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
        print(room_types, all_users)
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
        print(created_clean)
        for pk in created_clean:
            photo = room_models.Room.objects.get(pk=pk)
            print(photo)
        self.stdout.write(self.style.SUCCESS(f"{number} rooms Created!"))

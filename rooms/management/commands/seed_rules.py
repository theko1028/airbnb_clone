from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates house rules"

    """ def add_arguments(self, parser):
        parser.add_argument("--times", help="code testing...") """

    def handle(self, *args, **options):
        house_rules = [
            "No Parties or Events",
            "Only registered Guests",
            "No eating or drinking in the bedrooms",
            "Do the dishes",
            "No smoking",
            "Fake Tan = BYO Sheets",
            "Turn of lights and AC/Heating when out of the property",
            "No Pets",
        ]
        for h in house_rules:
            HouseRule.objects.create(name=h)
        self.stdout.write(
            self.style.SUCCESS(f"{len(house_rules)} House rules created!")
        )

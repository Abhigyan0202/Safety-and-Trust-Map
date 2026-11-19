
import csv
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from crime_data.models import PoliceStation


class Command(BaseCommand):
    help = "Import police stations from data.csv"

    def handle(self, *args, **options):
        csv_path = settings.BASE_DIR / "data.csv"

        if not csv_path.exists():
            raise CommandError(f"CSV file not found: {csv_path}")

        names = set()

        with csv_path.open(
            "r", encoding="utf-8-sig", newline=""
        ) as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames or "Name" not in reader.fieldnames:
                raise CommandError(
                    "CSV must contain a 'Name' column."
                )

            for row in reader:
                name = (row.get("Name") or "").strip()
                if name:
                    names.add(name)

        created_count = 0

        for name in sorted(names):
            _, created = PoliceStation.objects.get_or_create(
                name=name
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Found {len(names)} unique stations; "
                f"created {created_count} new records."
            )
        )

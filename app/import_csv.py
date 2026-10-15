import csv
import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from crime_data.models import Region_data

batch = []
batch_size = 500

with open("data.csv", "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        batch.append(
            Region_data(
                name=row["Name"].strip(),
                firs=int(float(row["FIRs"])),
                month=row["Month"].strip(),
                year=int(row["Year"]),
            )
        )

        if len(batch) >= batch_size:
            Region_data.objects.bulk_create(
                batch, batch_size=batch_size
            )
            batch.clear()

    if batch:
        Region_data.objects.bulk_create(
            batch, batch_size=batch_size
        )

print("CSV import completed!")
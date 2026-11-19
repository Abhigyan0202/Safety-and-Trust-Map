from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime_data', '0004_merge_20261119_1829'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                ALTER TABLE crime_data_region_reviews
                ADD COLUMN police_station_id INTEGER
                REFERENCES crime_data_policestation(id);
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
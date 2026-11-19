from django.db import migrations


def add_missing_coordinates(apps, schema_editor):
    RegionData = apps.get_model('crime_data', 'Region_data')
    table_name = RegionData._meta.db_table

    columns = {
        column.name
        for column in schema_editor.connection.introspection.get_table_description(
            schema_editor.connection.cursor(), table_name
        )
    }

    for field_name in ['latitude', 'longitude']:
        if field_name not in columns:
            field = RegionData._meta.get_field(field_name)
            schema_editor.add_field(RegionData, field)


class Migration(migrations.Migration):

    dependencies = [
        ('crime_data', '0002_alter_region_reviews_rating'),
    ]

    operations = [
        migrations.RunPython(
            add_missing_coordinates,
            migrations.RunPython.noop,
        ),
    ]
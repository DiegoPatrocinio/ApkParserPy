from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='position',
            field=geoposition.fields.GeopositionField(default=None, max_length=42),
            preserve_default=False,
        ),
    ]

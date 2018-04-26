from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0002_item_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.Category')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]

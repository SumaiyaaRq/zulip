# Generated by Django 5.0.10 on 2025-01-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0660_add_imageattachment_content_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="archivetransaction",
            name="protect_from_deletion",
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]

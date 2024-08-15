# Generated by Django 5.0.7 on 2024-07-29 04:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Big5App", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assessmentresponse",
            name="user_id",
            field=models.CharField(
                default=uuid.uuid4,
                editable=False,
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]

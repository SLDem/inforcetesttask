# Generated by Django 4.2.5 on 2023-09-12 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurants", "0002_menu_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="day",
            field=models.DateField(default=datetime.date(2023, 9, 12)),
        ),
    ]

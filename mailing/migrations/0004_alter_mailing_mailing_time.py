# Generated by Django 4.2.4 on 2023-09-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="mailing_time",
            field=models.DateTimeField(verbose_name="время рассылки"),
        ),
    ]

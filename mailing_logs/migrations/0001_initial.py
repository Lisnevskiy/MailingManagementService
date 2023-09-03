# Generated by Django 4.2.4 on 2023-09-03 19:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("recipient", "0002_initial"),
        ("mailing", "0004_alter_mailing_mailing_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="MailingLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "attempt_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата и время попытки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("successful", "Successful"), ("failed", "Failed")],
                        max_length=20,
                        verbose_name="Статус попытки",
                    ),
                ),
                (
                    "error_message",
                    models.TextField(
                        blank=True, null=True, verbose_name="Сообщение об ошибке"
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.mailing",
                        verbose_name="Рассылка",
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipient.recipient",
                        verbose_name="Получатель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Лог рассылки",
                "verbose_name_plural": "Логи рассылки",
            },
        ),
    ]

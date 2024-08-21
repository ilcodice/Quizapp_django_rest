# Generated by Django 5.1 on 2024-08-21 14:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("question", models.TextField(max_length=2000)),
                (
                    "select_level",
                    models.CharField(
                        choices=[("1", "Easy"), ("2", "Medium"), ("3", "Difficult")],
                        default="1",
                        max_length=40,
                    ),
                ),
                (
                    "select_topic",
                    models.CharField(
                        choices=[
                            ("Basics_1", "Data Types and Variables"),
                            ("Basics_2", "Control Flow"),
                            ("Functions and Modules", "Functions and Modules"),
                            ("Data Structures", "Data Structures"),
                            ("File Handling", "File Handling"),
                            (
                                "Error and Exception Handling",
                                "Error and Exception Handling",
                            ),
                            ("Advanced Data Structures", "Advanced Data Structures"),
                            ("OOP", "Object-Oriented Programming (OOP)"),
                        ],
                        default="Basics_1",
                        max_length=80,
                    ),
                ),
                (
                    "correct_answer",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1000), size=None
                    ),
                ),
                (
                    "incorrect_answer",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1000), size=None
                    ),
                ),
                (
                    "hint",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1000), size=None
                    ),
                ),
                ("score", models.SmallIntegerField()),
            ],
        ),
    ]

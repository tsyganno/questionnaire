# Generated by Django 4.0.3 on 2022-04-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0005_choice_correct_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='correct_answer',
            field=models.BooleanField(null=True),
        ),
    ]

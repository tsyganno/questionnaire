# Generated by Django 4.0.3 on 2022-04-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0004_choice_type_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='correct_answer',
            field=models.CharField(max_length=50, null=True, verbose_name='Правильный ответ'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0007_audioquestion_imagequestion_questiontype_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audioquestion',
            options={'verbose_name': 'Аудио вопрос', 'verbose_name_plural': 'Аудио вопросы'},
        ),
        migrations.AlterModelOptions(
            name='imagequestion',
            options={'verbose_name': 'Графический вопрос', 'verbose_name_plural': 'Графические вопросы'},
        ),
        migrations.AlterModelOptions(
            name='questiontype',
            options={'ordering': ['name'], 'verbose_name': 'Тип вопроса', 'verbose_name_plural': 'Типы вопросов'},
        ),
        migrations.AlterModelOptions(
            name='videoquestion',
            options={'verbose_name': 'Видео вопрос', 'verbose_name_plural': 'Видео вопросы'},
        ),
        migrations.RemoveField(
            model_name='audioquestion',
            name='name_question_audio',
        ),
        migrations.RemoveField(
            model_name='imagequestion',
            name='name_question_image',
        ),
        migrations.RemoveField(
            model_name='videoquestion',
            name='name_question_video',
        ),
        migrations.AddField(
            model_name='questiontype',
            name='name',
            field=models.CharField(max_length=150, null=True, verbose_name='Вопрос'),
        ),
    ]

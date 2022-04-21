from django.db import models


class Vote(models.Model):
    title = models.CharField(max_length=50, verbose_name='Опрос')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Опросы'
        verbose_name = 'Опрос'
        ordering = ['-published']


class QuestionType(models.Model):
    vote = models.ForeignKey('Vote', null=True, on_delete=models.CASCADE, verbose_name='Опрос')
    name = models.CharField(null=True, max_length=150, verbose_name='Вопрос')
    type_text = models.BooleanField(null=True, verbose_name='Текстовый вопрос')
    type_image = models.BooleanField(null=True, verbose_name='Графический вопрос')
    type_audio = models.BooleanField(null=True, verbose_name='Аудио вопрос')
    type_video = models.BooleanField(null=True, verbose_name='Видео вопрос')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Типы вопросов'
        verbose_name = 'Тип вопроса'
        ordering = ['name']


class ImageQuestion(models.Model):
    question = models.ForeignKey('QuestionType', null=True, on_delete=models.PROTECT, verbose_name='Вопрос')
    image = models.ImageField(upload_to='images/voting_app')
    correct_answer_image = models.CharField(max_length=50, verbose_name='Правильный ответ на графический вопрос')

    class Meta:
        verbose_name_plural = 'Графические вопросы'
        verbose_name = 'Графический вопрос'


class AudioQuestion(models.Model):
    question = models.ForeignKey('QuestionType', null=True, on_delete=models.PROTECT, verbose_name='Вопрос')
    audio = models.FileField(upload_to='audio/voting_app')
    correct_answer_audio = models.CharField(max_length=50, verbose_name='Правильный ответ на аудио вопрос')

    class Meta:
        verbose_name_plural = 'Аудио вопросы'
        verbose_name = 'Аудио вопрос'


class VideoQuestion(models.Model):
    question = models.ForeignKey('QuestionType', null=True, on_delete=models.PROTECT, verbose_name='Вопрос')
    video = models.FileField(upload_to='video/voting_app')
    correct_answer_video = models.CharField(max_length=50, verbose_name='Правильный ответ на видео вопрос')

    class Meta:
        verbose_name_plural = 'Видео вопросы'
        verbose_name = 'Видео вопрос'


class Choice(models.Model):
    question = models.ForeignKey('QuestionType', null=True, on_delete=models.PROTECT, verbose_name='Вопрос')
    choice_text = models.CharField(max_length=50, verbose_name='Выбор')
    correct_answer_choice = models.BooleanField(null=True, verbose_name='Правильный ответ')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name_plural = 'Варианты'
        verbose_name = 'Вариант'
        ordering = ['choice_text']

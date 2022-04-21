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


class Question(models.Model):
    vote = models.ForeignKey('Vote', null=True, on_delete=models.CASCADE, verbose_name='Опрос')
    name = models.TextField(null=True, blank=True, verbose_name='Вопрос')
    type = models.ForeignKey('TypeQuestion', null=True, on_delete=models.CASCADE, verbose_name='Тип вопроса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'
        ordering = ['name']


class TypeQuestion(models.Model):
    name_type = models.CharField(max_length=20, db_index=True, verbose_name='Тип вопроса')

    def __str__(self):
        return self.name_type

    class Meta:
        verbose_name_plural = 'Типы вопросов'
        verbose_name = 'Тип вопроса'
        ordering = ['name_type']


class Choice(models.Model):
    question = models.ForeignKey('Question', null=True, on_delete=models.PROTECT, verbose_name='Вопрос')
    choice_text = models.CharField(max_length=50, verbose_name='Выбор')
    votes = models.IntegerField(default=0)
    type_question = models.ForeignKey('TypeQuestion', null=True, on_delete=models.CASCADE, verbose_name='Тип вопроса')
    correct_answer = models. BooleanField(null=True, verbose_name='Правильный ответ')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name_plural = 'Варианты'
        verbose_name = 'Вариант'
        ordering = ['choice_text']

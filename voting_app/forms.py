from django.forms import ModelForm
from .models import Question, Vote, TypeQuestion, Choice


class ChoiceForm(ModelForm):

    class Meta:
        model = Choice
        fields = ('choice_text', 'question', 'type_question', 'correct_answer')


class TypeQuestionForm(ModelForm):

    class Meta:
        model = TypeQuestion
        fields = ('name_type',)


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ('name', 'vote', 'type')


class VoteForm(ModelForm):

    class Meta:
        model = Vote
        fields = ('title', 'content')

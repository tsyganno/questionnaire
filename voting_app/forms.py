from django.forms import ModelForm
from django import forms
from .models import Vote, QuestionType, Choice, ImageQuestion, AudioQuestion


class AudioQuestionForm(forms.ModelForm):

    class Meta:
        model = AudioQuestion

        fields = ('question', 'audio', 'correct_answer_audio')

    def __init__(self, *args, **kwargs):
        super(AudioQuestionForm, self).__init__(*args, **kwargs)
        self.fields['question'].queryset = QuestionType.objects.filter(type_text=False, type_image=False, type_audio=True, type_video=False)


class ImageQuestionForm(forms.ModelForm):

    class Meta:
        model = ImageQuestion

        fields = ('question', 'image', 'correct_answer_image')

    def __init__(self, *args, **kwargs):
        super(ImageQuestionForm, self).__init__(*args, **kwargs)
        self.fields['question'].queryset = QuestionType.objects.filter(type_text=False, type_image=True, type_audio=False, type_video=False)


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice

        fields = ('question', 'choice_text', 'correct_answer_choice')

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.fields['question'].queryset = QuestionType.objects.filter(type_text=True, type_image=False, type_audio=False, type_video=False)


class VoteForm(ModelForm):

    class Meta:
        model = Vote
        fields = ('title', 'content')


class QuestionTypeForm(ModelForm):

    class Meta:
        model = QuestionType
        fields = ('vote', 'name', 'type_text', 'type_image', 'type_audio', 'type_video')

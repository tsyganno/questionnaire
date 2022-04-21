from django.forms import ModelForm
from .models import Vote, QuestionType


class VoteForm(ModelForm):

    class Meta:
        model = Vote
        fields = ('title', 'content')


class QuestionTypeForm(ModelForm):

    class Meta:
        model = QuestionType
        fields = ('vote', 'name', 'type_text', 'type_image', 'type_audio', 'type_video')

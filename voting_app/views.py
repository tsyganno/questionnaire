from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Модуль для создания нового пользователя и входа уже существующего
from django.contrib.auth.models import User  # Модуль для создания модели пользователя
from django.db import IntegrityError  # Импортируем IntegrityError для исключения ввода уже существющих данных пользователя
from django.contrib.auth import login, logout, authenticate  # Добавляем функции login, logout и authenticate для входа, выхода и аутенфикации пользователя
from rest_framework import generics
from .serializers import UserSerializer
from .models import Vote, QuestionType, Choice, ImageQuestion
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import VoteForm, QuestionTypeForm, ChoiceForm, ImageQuestionForm, AudioQuestionForm
from django.http import HttpResponseNotFound, HttpResponseServerError


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')


def audio_type(request):
    return render(request, 'voting_app/audio_type.html')


def image_type(request):
    images = ImageQuestion.objects.filter(question__type_text=False, question__type_image=True, question__type_audio=False, question__type_video=False)
    global_dict = {}
    answer_dict = {}
    for image in images:
        vote = image.question.vote.title
        question = image.question.name
        answer = image.correct_answer_image
        if question not in answer_dict:
            answer_dict[question] = answer
        if vote not in global_dict:
            global_dict[vote] = global_dict.setdefault(vote, {})
            if question not in global_dict[vote]:
                global_dict[vote][question] = global_dict[vote].setdefault(question, [image.image])
        else:
            if question not in global_dict[vote]:
                global_dict[vote][question] = global_dict[vote].setdefault(question, [image.image])
            else:
                global_dict[vote][question].append(image.image)
    return render(request, 'voting_app/image_type.html', {'global_dict': global_dict, 'answer_dict': answer_dict})


def text_type(request):
    choices = Choice.objects.filter(question__type_text=True, question__type_image=False, question__type_audio=False, question__type_video=False)
    global_dict = {}
    for choice in choices:
        vote = choice.question.vote.title
        question = choice.question.name
        if vote not in global_dict:
            global_dict[vote] = global_dict.setdefault(vote, {})
            if question not in global_dict[vote]:
                global_dict[vote][question] = global_dict[vote].setdefault(question, [choice.choice_text])
        else:
            if question not in global_dict[vote]:
                global_dict[vote][question] = global_dict[vote].setdefault(question, [choice.choice_text])
            else:
                global_dict[vote][question].append(choice.choice_text)
    return render(request, 'voting_app/text_type.html', {'global_dict': global_dict})


def question(request):
    questions = QuestionType.objects.all()
    dict_vote = {}
    for el in questions:
        if el.vote.title not in dict_vote:
            dict_vote[el.vote.title] = [el]
        else:
            dict_vote[el.vote.title].append(el)
    return render(request, 'voting_app/question.html', {'dict_vote': dict_vote})


class AudioQuestionCreateView(CreateView):
    template_name = 'voting_app/audio_type.html'
    form_class = AudioQuestionForm
    success_url = reverse_lazy('vote_app:audio_type')


class ImageQuestionCreateView(CreateView):
    template_name = 'voting_app/image_type.html'
    form_class = ImageQuestionForm
    success_url = reverse_lazy('vote_app:image_type')


class ChoiceCreateView(CreateView):
    template_name = 'voting_app/text_type.html'
    form_class = ChoiceForm
    success_url = reverse_lazy('vote_app:text_type')


class QuestionTypeCreateView(CreateView):
    template_name = 'voting_app/question.html'
    form_class = QuestionTypeForm
    success_url = reverse_lazy('vote_app:question')


class VoteCreateView(CreateView):
    template_name = 'voting_app/personal_area_user.html'
    form_class = VoteForm
    success_url = reverse_lazy('vote_app:personal_area_user')


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def home(request):
    """Функция возвращает шаблон домашней страницы"""
    return render(request, 'voting_app/home.html')


def authentication_user(request):
    """Функция создает пользователя и переводит его в личный кабинет"""
    if request.method == 'GET':
        return render(request, 'voting_app/authentication_user.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('vote_app:personal_area_user')
            except IntegrityError:
                return render(request, 'voting_app/authentication_user.html', {'form': UserCreationForm(), 'error': 'Это имя пользователя уже используется, задайте другое.'})
        else:
            return render(request, 'voting_app/authentication_user.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают, попробуйте еще раз.'})


def login_user(request):
    """Функция входа пользователя"""
    if request.method == 'GET':
        return render(request, 'voting_app/login_user.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'voting_app/login_user.html', {'form': AuthenticationForm(), 'error': 'Пользователя с таким паролем не существует.'})
        else:
            login(request, user)
            print('ok')
            return redirect('vote_app:personal_area_user')


def logout_user(request):
    """Функция при выходе из личного кабинета пользователя перенаправляет его на домашнюю страницу"""
    if request.method == 'POST':
        logout(request)
        return redirect('vote_app:home')


def personal_area_user(request):
    """Функция возвращает личный кабинет пользователя"""
    votes = Vote.objects.all()[:5]
    return render(request, 'voting_app/personal_area_user.html', {'votes': votes})


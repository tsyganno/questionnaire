from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Модуль для создания нового пользователя и входа уже существующего
from django.contrib.auth.models import User  # Модуль для создания модели пользователя
from django.db import IntegrityError  # Импортируем IntegrityError для исключения ввода уже существющих данных пользователя
from django.contrib.auth import login, logout, authenticate  # Добавляем функции login, logout и authenticate для входа, выхода и аутенфикации пользователя
from rest_framework import generics
from .serializers import UserSerializer
from .models import Vote, Question, TypeQuestion, Choice
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import QuestionForm, VoteForm, TypeQuestionForm, ChoiceForm


def type_question(request):
    types = TypeQuestion.objects.all()[:5]
    return render(request, 'voting_app/type_question.html', {'types': types})


def type_answer(request):
    answer_questions = Question.objects.filter(type__name_type='ответ')
    answers = Choice.objects.filter(correct_answer=True)
    return render(request, 'voting_app/answer_question.html', {'answers': answers, 'answer_questions': answer_questions})


def type_test(request):
    test_questions = Question.objects.filter(type__name_type='тест')
    choices = Choice.objects.all()
    answers = Choice.objects.filter(correct_answer=True)
    dict_choices = {}
    for question in test_questions:
        for choice in choices:
            if choice.question.name == question.name:
                if choice.question.name not in dict_choices:
                    dict_choices[question.name] = [choice.choice_text]
                else:
                    dict_choices[question.name].append(choice.choice_text)
    return render(request, 'voting_app/test_question.html', {'dict_ch': dict_choices, 'questions': test_questions, 'answers': answers})


def personal_area_user_question(request):
    """Функция возвращает личный кабинет пользователя c вопросами к опросу"""
    table = Question.objects.select_related('vote').all()
    dict_all = {}
    for question in table:
        if question.vote.title not in dict_all:
            dict_all[question.vote.title] = [question.name]
        else:
            dict_all[question.vote.title].append(question.name)
    return render(request, 'voting_app/question.html', {'dict': dict_all})


class AnswerCreateView(CreateView):
    template_name = 'voting_app/answer_question.html'
    form_class = ChoiceForm
    success_url = reverse_lazy('vote_app:type_answer')


class ChoiceCreateView(CreateView):
    template_name = 'voting_app/test_question.html'
    form_class = ChoiceForm
    success_url = reverse_lazy('vote_app:type_test')


class TypeQuestionCreateView(CreateView):
    template_name = 'voting_app/type_question.html'
    form_class = TypeQuestionForm
    success_url = reverse_lazy('vote_app:type_question')


class VoteCreateView(CreateView):
    template_name = 'voting_app/personal_area_user.html'
    form_class = VoteForm
    success_url = reverse_lazy('vote_app:personal_area_user')


class QuestionCreateView(CreateView):
    template_name = 'voting_app/question.html'
    form_class = QuestionForm
    success_url = reverse_lazy('vote_app:personal_area_user_question')


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
    types = TypeQuestion.objects.all()
    votes = Vote.objects.all()[:5]
    return render(request, 'voting_app/personal_area_user.html', {'votes': votes, 'types': types})


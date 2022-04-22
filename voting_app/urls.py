from django.urls import path
from voting_app.views import authentication_user, login_user, logout_user, home, personal_area_user, UserList, \
    UserDetail, VoteCreateView, question, QuestionTypeCreateView, text_type, ChoiceCreateView, image_type, \
    ImageQuestionCreateView, audio_type, AudioQuestionCreateView


app_name = 'vote_app'
urlpatterns = [

    # Аутентификация
    path('authentication/', authentication_user, name='authentication_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),

    # Личный кабинет
    path('', home, name='home'),
    path('personal_area/', personal_area_user, name='personal_area_user'),
    path('personal_area/add_vote', VoteCreateView.as_view(), name='add_vote'),
    path('personal_area/question/', question, name='question'),
    path('personal_area/question/add_question', QuestionTypeCreateView.as_view(), name='add_question'),
    path('personal_area/question/text_type', text_type, name='text_type'),
    path('personal_area/question/text_type/add_choices/', ChoiceCreateView.as_view(), name='add_choices'),
    path('personal_area/question/image_type', image_type, name='image_type'),
    path('personal_area/question/image_type/add_image/', ImageQuestionCreateView.as_view(), name='add_image'),
    path('personal_area/question/audio_type', audio_type, name='audio_type'),
    path('personal_area/question/audio_type/add_audio/', AudioQuestionCreateView.as_view(), name='add_audio'),


    # api
    path('api/list/', UserList.as_view()),
    path('api/list/<int:pk>/', UserDetail.as_view()),

]

from django.urls import path
from voting_app.views import QuestionCreateView, authentication_user, login_user, logout_user, home, \
    personal_area_user, UserList, UserDetail, VoteCreateView, personal_area_user_question, type_question, \
    TypeQuestionCreateView,  type_test, ChoiceCreateView, type_answer, AnswerCreateView


app_name = 'vote_app'
urlpatterns = [

    # Аутентификация
    path('authentication/', authentication_user, name='authentication_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),

    # Личный кабинет
    path('', home, name='home'),
    path('personal_area/', personal_area_user, name='personal_area_user'),
    path('personal_area/question/', personal_area_user_question, name='personal_area_user_question'),
    path('personal_area/add_vote/', VoteCreateView.as_view(), name='add_vote'),
    path('personal_area/add_question/', QuestionCreateView.as_view(), name='add_question'),

    # Типы вопросов type_answer
    path('personal_area/question/type/', type_question, name='type_question'),
    path('personal_area/question/add_type/', TypeQuestionCreateView.as_view(), name='add_type_question'),
    path('personal_area/question/type/test/', type_test, name='type_test'),
    path('personal_area/question/type/answer/', type_answer, name='type_answer'),
    path('personal_area/question/type/test/add_choices/', ChoiceCreateView.as_view(), name='add_choices'),
    path('personal_area/question/type/answer/add_choices/', AnswerCreateView.as_view(), name='add_answer'),

    # api
    path('api/list/', UserList.as_view()),
    path('api/list/<int:pk>/', UserDetail.as_view()),

]

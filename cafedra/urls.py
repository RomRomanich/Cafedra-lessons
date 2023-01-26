from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('logout/', LoginUser.as_view(), name='logout'),

    path('central/', central, name='central'),

    path('lessons/', LessonsList.as_view(), name='lessonslist'),
    path('lessons_search/', SearchLessonsView.as_view(), name='lessons_search'),
    path('lessons_search_date/', SearchLessonsViewDate.as_view(), name='lessons_search_date'),
    path('lessons_add/', AddLessonsPage.as_view(), name='lessons_add'),

    path('referat/', ReferatList.as_view(), name='referatlist'),
    path('referat_search/', SearchReferatView.as_view(), name='referat_search'),
    path('referat_search_date/', SearchReferatViewDate.as_view(), name='referat_search_date'),
    path('referatspravka_add/', AddReferatPage.as_view(), name='referat_add'),

    path('order/', cafedra_order, name='cafedra_order'),
    path('cafedra_1/', cafedra_1, name='cafedra_1'),
    path('cafedra_2/', cafedra_2, name='cafedra_2'),

]

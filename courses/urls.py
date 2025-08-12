from django.urls import path
from courses.views.course_views import *
from courses.views.exam_views import *

app_name="courses"
urlpatterns=[
    #course pattern
    path('all',course_list,name='course-list'),
    path('<int:pk>',CoureseDetailUpdateDeleteView.as_view(),name='course_detail'),
    #exam pattern
    path('exam/all',ExamListCreateView.as_view(),name='exam-list'),
    path('exam/<slug:pk>',ExamDetailUpdateDeleteView.as_view(),name="exam_delete")
]
"""wspexam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from wspexamapp.views import PupilLoginView, TeacherLoginView, QuestionsPageView, ExamPageView

urlpatterns = [
    path('', PupilLoginView.as_view(), name='login'),
    path('Exam/<int:pk>/', ExamPageView.as_view(), name='exam'),
    path('TeacherPortal/', TeacherLoginView.as_view(), name='teacher_portal'),
    path('ExamSetup/<int:pk>/', QuestionsPageView.as_view(), name='exam_setup'),
]

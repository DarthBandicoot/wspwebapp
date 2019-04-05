from django.contrib import admin


# Register your models here.
from .models import Pupil, Teacher, ExamQuestions, Exam


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass


@admin.register(ExamQuestions)
class ExamQuestionsAdmin(admin.ModelAdmin):
    pass


from django.contrib import admin

# Register your models here.
from .models import Pupil, Teacher


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


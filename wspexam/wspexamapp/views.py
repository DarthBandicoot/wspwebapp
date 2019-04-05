from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from wspexamapp.forms import PupilLoginForm, TeacherLoginForm, ExamPageForm
from wspexamapp.models import Pupil, Teacher


class PupilLoginView(FormView):
    form_class = PupilLoginForm
    template_name = 'generic_form.html'
    model = Pupil
    user = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_header'] = 'Login Page'
        context['help_text'] = 'If this is first time logging in a user account is created on form submission'

        return context

    def form_valid(self, form):
        user_firstname = form.cleaned_data.get('first_name')
        user_lastname = form.cleaned_data.get('last_name')
        user_email = form.cleaned_data.get('email')

        return super().form_valid(form)


class TeacherLoginView(FormView):
    form_class = TeacherLoginForm
    template_name = 'generic_form.html'
    model = Teacher
    user = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_header'] = 'Login Page'
        context['help_text'] = 'If this is first time logging in a user account is created on form submission'

        return context

    def form_valid(self, form):
        admin_username = form.cleaned_data.get('username')
        admin_password = form.cleaned_data.get('password')

        return super().form_valid(form)


class ExamPageView(FormView):
    form_class = ExamPageForm
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def form_valid(self, form):
        return super().form_valid(form)

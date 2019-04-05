from django.views.generic import FormView

from wspexamapp.forms import PupilLoginForm
from wspexamapp.models import Pupil


class PupilLoginView(FormView):
    form_class = PupilLoginForm
    template_name = 'login.html'
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


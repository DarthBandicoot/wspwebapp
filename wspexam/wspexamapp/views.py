from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from wspexamapp.forms import PupilLoginForm, TeacherLoginForm, ExamPageForm, ExamQuestionsForm
from wspexamapp.models import Pupil, Teacher, ExamQuestions, ExamResults


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

    def get_redirect_url(self):
        """
        will redirect to teacher portal instead
        :return:
        """
        return reverse_lazy(
            'teacher_portal'
        )

    def form_valid(self, form):
        user_firstname = form.cleaned_data.get('first_name')
        user_lastname = form.cleaned_data.get('last_name')
        user_email = form.cleaned_data.get('email')

        if 'isteacher' in self.request.POST:
            self.get_redirect_url()
            return HttpResponseRedirect(self.get_redirect_url())

        if self.check_user_exists(user_firstname, user_email) == 'False':
            self.user = Pupil(first_name=user_firstname,
                              last_name=user_lastname,
                              email_address=user_email)
            self.user.save()

        else:
            self.user = Pupil.objects.get(email_address=user_email)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('exam', kwargs={'pk', self.request.user})

    def check_user_exists(self, name, email):
        """
        will take parameters to check if user exists will create user based on value returned
        :param name:
        :param email:
        :return:
        """
        user_exist = Pupil.objects.filter(first_name=name,
                                          email_address=email)
        if user_exist.count() >= 1:
            return 'True'
        return 'False'


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

        if self.check_user_exists(admin_username) == 'False':
            self.user = Teacher(username=admin_username,
                                password=admin_password)

            self.user.save()
        else:
            self.user = Teacher.objects.get(username=admin_username,
                                            password=admin_password)

        return super().form_valid(form)

    def check_user_exists(self, user):

        user_exist = Teacher.objects.filter(username=user)

        if user_exist.count() >= 1:
            return 'True'
        return 'False'

    def get_success_url(self):

        return reverse_lazy('exam_setup', kwargs={'pk': self.user.id})


class ExamPageView(FormView):
    form_class = ExamPageForm
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def form_valid(self, form):
        return super().form_valid(form)


class QuestionsPageView(FormView):
    form_class = ExamQuestionsForm
    template_name = 'generic_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_header'] = 'Exam Configuration'
        context['question_add_text'] = 'Please Add New Questions to the Exam, ' \
                                       'Only one Question Type may be added at a time'

        return context

    def form_valid(self, form):
        multiple_question = form.cleaned_data.get('multiple_question')
        multi_choice1 = form.cleaned_data.get('multi_choice1')
        multi_choice2 = form.cleaned_data.get('multi_choice2')
        multi_choice3 = form.cleaned_data.get('multi_choice3')
        correct_answer = form.cleaned_data.get('correct_answer')
        single_question = form.cleaned_data.get('single_question')
        single_choice = form.cleaned_data.get('single_choice')
        score = form.cleaned_data.get('score')

        if len(multiple_question) > 0:
            ExamQuestions(question=multiple_question,
                          multi_choice1=multi_choice1,
                          multi_choice2=multi_choice2,
                          multi_choice3=multi_choice3,
                          correct_answer=correct_answer,
                          score=score)

        elif len(single_question) > 0:
            ExamQuestions(question=single_question,
                          correct_answer=single_choice,
                          score=score)

        return super().form_valid(form)


class ExamScoresView(ListView):
    model = ExamResults
    context_object_name = 'results_list'
    template_name = 'scores.html'
    
    def get_queryset(self):
        queryset = ExamResults.objects.all()

        return queryset


from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field
from django import forms
from django.core.exceptions import ValidationError

from wspexamapp.models import Teacher, Exam


class PupilLoginForm(forms.Form):
    first_name = forms.CharField(max_length=250, required=False)
    last_name = forms.CharField(max_length=250, required=False)
    email = forms.CharField(max_length=250, required=False)
    exam = forms.ModelChoiceField(queryset=Exam.objects.all(), required=False,
                                  label="Please Select Exam to Continue")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'main_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            Fieldset(
                "User Login",
                Field('first_name'),
                Field('last_name'),
                Field('email'),
                Field('exam'),
            ),
            FormActions(
                Submit('save', 'Login'),
                Submit('isteacher', 'Teacher Login Portal', css_class='btn-info')
            )
        )

    def clean(self):
        exam_choice = self.cleaned_data.get('exam')

        if not exam_choice:
            raise ValidationError('Please Select Exam')


class TeacherLoginForm(forms.Form):
    username = forms.CharField(max_length=250, required=True)
    password = forms.CharField(max_length=250, required=True, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'main_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            Fieldset(
                "Teacher Login",
                Field('username'),
                Field('password'),
            ),
            FormActions(
                Submit('save', 'Login'),
            )
        )

    def clean(self):
        user_check = Teacher.objects.get(username=self.cleaned_data.get('username'))

        if user_check:
            if user_check.password != self.cleaned_data.get('password'):
                raise ValidationError('Password Incorrect')


class ExamPageForm(forms.Form):
    questions = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'main_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            Fieldset(
                "Questions",

            ),
            FormActions(
                Submit('save', 'Submit Exam')
            )
        )

    def clean(self):
        pass


class ExamQuestionsForm(forms.Form):
    single_question = forms.CharField(max_length=200, required=False)
    single_choice = forms.CharField(max_length=200, required=False)
    multiple_question = forms.CharField(max_length=200, required=False)
    multi_choice1 = forms.CharField(max_length=200, required=False)
    multi_choice2 = forms.CharField(max_length=200, required=False)
    multi_choice3 = forms.CharField(max_length=200, required=False)
    correct_answer = forms.CharField(max_length=200, required=False)
    score = forms.FloatField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'main_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            Fieldset(
                "Single Answer Question",
                Field('single_question'),
                Field('single_choice'),
            ),
            Fieldset(
                "Multi Answer Question",
                Field('multiple_question'),
                Field('multi_choice1'),
                Field('multi_choice2'),
                Field('multi_choice3'),
                Field('correct_answer'),
            ),
            Fieldset(
                "Score For Question",
                Field('score'),
            ),
            FormActions(
                Submit('save', 'Save Question and Logout'),
                Submit('save', 'Save Question and add another', css_class='btn-info'),
            )
        )

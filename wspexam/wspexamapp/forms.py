from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field
from django import forms


class PupilLoginForm(forms.Form):
    first_name = forms.CharField(max_length=250, required=False)
    last_name = forms.CharField(max_length=250, required=False)
    email = forms.CharField(max_length=250, required=False)

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
                Field('email')
            ),
            FormActions(
                Submit('save', 'Login'),
                Submit('isteacher', 'Teacher Login Portal', css_class='btn-info')
            )
        )

    def clean(self):
        pass

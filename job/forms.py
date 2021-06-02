from django import forms
from .models import Apply, Job


class Apply_form(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','website','upload_cv','cover_leter']


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner','slug')
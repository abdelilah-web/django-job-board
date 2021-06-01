from django import forms
from .models import Apply


class Apply_form(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','website','upload_cv','cover_leter']
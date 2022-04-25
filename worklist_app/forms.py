from django import forms
from django.forms import models
from .models import List


class DateInput(forms.DateInput):
    input_type = 'date'

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed", "date"]
        widgets = {"date": DateInput()}
        # date = {'my_date_field' : DateInput()}
from django import forms
from .models import Question

class DateInput(forms.DateInput):
    input_type = 'date'

class QuestionForm(forms.ModelForm):
    site = forms.CharField(disabled=True,initial="stackoverflow")
    # filter = forms.CharField(disabled=True,initial="withbody")
    fromdate = forms.DateField(widget=DateInput, required=False)
    todate = forms.DateField(widget=DateInput, required=False)
    min = forms.DateField(widget=DateInput, required=False)
    max = forms.DateField(widget=DateInput, required=False)
    class Meta:
        model = Question
        fields = "__all__"
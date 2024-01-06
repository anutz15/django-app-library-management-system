from django import forms
import datetime
from issuebook.models import issuedbooks

class issueform(forms.Form):
    rollnumber=forms.CharField()
    number_of_copies=forms.IntegerField()
    reason_for_issue=forms.Textarea()
    date_of_issue=forms.DateField(initial=datetime.date.today(),widget=forms.SelectDateWidget())
    date_of_submission=forms.DateField(widget=forms.SelectDateWidget())

class issueformmodel(forms.ModelForm):
    date_of_issue=forms.DateField(initial=datetime.date.today(),widget=forms.SelectDateWidget())
    date_of_submission=forms.DateField(initial=datetime.date.today(),widget=forms.SelectDateWidget())
    class Meta:
        model=issuedbooks
        fields="__all__"
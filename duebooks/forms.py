from django import forms

class getrollnuoform(forms.Form):
    rollno=forms.CharField()


class amountform(forms.Form):
    bookid=forms.CharField()
    amt=forms.IntegerField()
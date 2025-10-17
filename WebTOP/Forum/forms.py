from django import forms


class ThreadForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()


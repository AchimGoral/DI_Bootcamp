from django import forms

class Todoform(forms.Form):
    title = forms.CharField(max_length=100, required=True, widget = forms.TextInput(
        attrs={
            'placeholder': 'Write your title'
        })
    )
    details = forms.CharField(widget = forms.Textarea(
        attrs={
            'placeholder': 'Write your details'
        })
    )
    has_been_done = forms.BooleanField(required=False)
    deadline_date = forms.DateTimeField(widget = forms.SelectDateWidget)
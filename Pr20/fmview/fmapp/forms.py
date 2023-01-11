from django import forms


class feedbackform(forms.Form):
    Name = forms.CharField(max_length=33)
    review = forms.CharField(widget=forms.Textarea)
    stars = forms.IntegerField()

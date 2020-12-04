from django import forms

from .models import Topping, Comment, Pizza

class ToppingForm(forms.ModelForm):
    class Meta:
        Model = Topping #model you're going to use
        fields = ['name']
        labels = {'name':''}
        widgets = {'name': forms.Textarea(attrs={'cols': 80})}

class CommentForm(forms.ModelForm):
    class Meta:
        Model = Comment
        fields = ['name']
        labels = {'name':''}

from tkinter import Widget
from django import forms
from .models import Coment, Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:

    choice_list.append(item)
    




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'header_imag','category', 'body', 'snippet')

        Widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control',  'value': ' ', 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'snippet')

        Widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ['name','body']

        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            
            'body': forms.TextInput(attrs={'class': 'form-control'}),

        }
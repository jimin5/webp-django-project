from django import forms 
from .models import Post, Comment, Categori

class Postform(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class CategoriForm(forms.ModelForm):
    class Meta:
        model = Categori
        fields=('categori_name',)

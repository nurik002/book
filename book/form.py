from django import forms

from book.models import CommentModel


class CommentFormsModel(forms.ModelForm):
    class Meta:
        exclude = ['book', 'user']
        model = CommentModel

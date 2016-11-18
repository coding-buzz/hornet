from django import forms

import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        exclude = ['blog_post', 'created_at']

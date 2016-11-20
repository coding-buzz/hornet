from django import forms

from captcha.fields import ReCaptchaField

import models


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = models.Comment
        exclude = ['blog_post', 'created_at']

from django import forms
from .models import Article, BlogComment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['user_name', 'body']

        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入昵称",
                'aria-describedby': "sizing-addon1",
            }),
            'body': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入评价",
                'aria-describedby': "sizing-addon1",
            }),
        }

from django import forms
from cms.models import Blog_post

class Blog_postForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text = 'title :')
    post_text = forms.CharField(widget=forms.Textarea, help_text = 'content :')

    class Meta:
        model = Blog_post
        fields = ('title', 'post_text')
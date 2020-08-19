
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = '__all__'
        widgets = {
            'tags':forms.TextInput(attrs={'class':'py-2 my-2 w-full border border-indigo-500'}),
            'title':forms.TextInput(attrs={'class':'py-2 my-2 w-full border border-indigo-500'}),
            'Blog_title_tag':forms.TextInput(attrs={'class':'py-2 my-2 w-full border border-indigo-500'}),
            'image':forms.TextInput(attrs={'class':'py-2 my-2 w-full border border-indigo-500'}),
            'pub_date':forms.TextInput(attrs={'class':'py-2 my-2 w-full border border-indigo-500'}),
            'body':forms.Textarea(attrs={'class':'py-2 my-2 w-full border border-indigo-500'}),
            'author':forms.Select(attrs={'class':'py-2 my-2 w-full border border-indigo-500'})

        }

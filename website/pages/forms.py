from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ('title','pub_date','tags','body','image')
        widgets ={
            'title':forms.TextInput(attrs={'class':'border border-2 rounded-r px-4 py-2 my-2 w-full', 'placeholder':'Enter a Tile','label': 'Your name'}),
            'pub_date':forms.TextInput(attrs={'class':'border border-2 rounded-r px-4 py-2 my-2 w-full', 'placeholder':'Enter Date, 2050-01-31'}),
            'tags':forms.TextInput(attrs={'class':'border border-2 rounded-r px-4 py-2 my-2 w-full', 'placeholder':'Enter a Tag'}),
            'body':forms.Textarea(attrs={'class':'form-textarea border border-2 rounded-r px-4 my-2 w-full h-20', 'placeholder':'Enter text'}  ),
            'image':forms.TextInput(attrs={'class':'form-textarea border border-2 rounded-r px-4 my-2 w-full h-20', 'placeholder':'Enter text'}  ),


        }

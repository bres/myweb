
from django import forms
from .models import Post,Category


choices=Category.objects.all().values_list('name','name')
choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = '__all__'
        widgets = {
            'tags':forms.TextInput(attrs={'class':'py-2 my-2 w-full border border-indigo-300 rounded','placeholder':'Insert the Tag category'}),
            'title':forms.TextInput(attrs={'class':'py-2 my-2 w-full border border-indigo-300 rounded','placeholder':'Insert the Title of Post'}),
            'Blog_title_tag':forms.TextInput(attrs={'class':'pt-2 my-2 w-full border border-indigo-300 rounded','placeholder':'Insert the Title Tag for page'}),
            #'image':forms.ImageField(),
            'pub_date':forms.TextInput(attrs={'class':'py-2 my-2 w-full border border-indigo-300 rounded','placeholder':'2050-12-31'}),
            'body':forms.Textarea(attrs={'class':'py-2 my-2 w-full border border-indigo-300 rounded','rows':3, 'cols': 100,'placeholder':'Insert the main text' }),
            'author':forms.Select(attrs={'class':'pt-2 mt-2 mb-10 w-full border border-indigo-300 rounded','placeholder':'Insert the name of the Author'}),
            'category':forms.Select(choices=choice_list ,attrs={'class':'pt-2 mt-2 mb-10 w-full border border-indigo-300 rounded','placeholder':'Select a category'})

        }

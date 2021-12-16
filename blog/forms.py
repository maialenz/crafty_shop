''' Form file for blog '''
from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, Postcategory, Comment


class PostForm(forms.ModelForm):
    '''form to add a new post'''
    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        postcategories = Postcategory.objects.all()
        friendly_names =\
            [(c.id, c.get_friendly_name()) for c in postcategories]

        self.fields['postcategory'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border rounded'


class PostcategoryForm(forms.ModelForm):
    ''' form for category'''
    class Meta:
        model = Postcategory
        fields = ('name', 'friendly_name')


class CommentForm(forms.ModelForm):
    ''' form to add comment '''
    class Meta:
        model = Comment
        fields = ('name', 'body')

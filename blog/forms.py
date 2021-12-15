from django import forms
from .models import Post, Postcategory, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        postcategories = Postcategory.objects.all()
        friendly_names =\
            [(c.id, c.get_friendly_name()) for c in postcategories]

        self.fields['postcategory'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class PostcategoryForm(forms.ModelForm):

    class Meta:
        model = Postcategory
        fields = ('name', 'friendly_name')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

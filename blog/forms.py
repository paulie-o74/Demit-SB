from django import forms
from .models import Comment, Post
from .widgets import CustomClearableFileInput



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'body': 'What are your thoughts?',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-product-form border-navy text-navy'
            self.fields[field].label = False


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'slug',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Journal entry title',
            'content': 'Main content',
            'status': 'Status',
        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-product-form border-navy text-navy'

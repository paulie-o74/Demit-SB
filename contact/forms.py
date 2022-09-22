from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form class
    """
    class Meta:
        """
        Meta class for shbow fields
        """
        model = Contact
        fields = ('first_name', 'second_name', 'email', 'phone_number',
                  'message',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'second_name': 'Second Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'message': 'Message',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'add-product-form \
                                                        border-navy text-navy'
            self.fields[field].label = False

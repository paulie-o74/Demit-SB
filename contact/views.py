from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def contact(request):
    """
    Shows and submits the contact form.
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = "Website enquiry"
            body = {
                    'first_name': contact_form.cleaned_data['first_name'],
                    'second_name': contact_form.cleaned_data['second_name'],
                    'email': contact_form.cleaned_data['email'],
                    'phone_number': contact_form.cleaned_data['phone_number'],
                    'message': contact_form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                          ['pauloriordan74@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            contact_form.save()
            messages.success(request,
                             ('Message received!'
                              'We will be in contact with you soon. '
                              'Thanks for reaching out.'))
            return redirect(reverse('contact'))
        else:
            messages.error(request,
                           ('Ooops! Something went wrong. '
                            'Please ensure the form is valid.'))
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'

    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)

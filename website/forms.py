from django import forms
from .models import ContactForm


class ContactFormCreate(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'message': forms.Textarea(attrs={'cols': 30, 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'id': 'name', 'placeholder': 'Name'})
        self.fields['email'].widget.attrs.update({'type': 'email', 'class': 'form-control', 'id': 'email', 'placeholder': 'Email'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'id': 'subject', 'placeholder': 'Subject'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'id': 'message', 'placeholder': 'Message'})

    def send_email(self):
        pass
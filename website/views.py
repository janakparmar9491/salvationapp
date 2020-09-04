from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, FormView
from .models import ContactForm
from .forms import ContactFormCreate
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail

# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'

class AboutPage(TemplateView):
    template_name = 'about.html'

class AllBlogPage(TemplateView):
    template_name = 'blog.html'

class BlogPage(TemplateView):
    template_name = 'blog-single.html'

# class ContactPage(FormView):
#     template_name = 'contact.html'
#     contactform = ContactFormCreate
#
#     def __init__(self, *args, **kwargs):
#         context = {}
#         context['form'] = ContactFormCreate()
#         return render(self.request, "contact.html", context)
#
#     def form_valid(self, form):
#         form.send_email()
#         return super(ContactPage, self).form_valid()

def contact_page(request):
    context ={}
    context['form']= ContactFormCreate()
    if request.method == 'POST':
        contactform = ContactFormCreate(request.POST)
        if contactform.is_valid():
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            from_email = request.POST.get('email', '')
            contactform.save()
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, ['janakparmar9491@gmail.com'], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                #return HttpResponseRedirect('/contact/thanks/')
            else:
                # In reality we'd use a form class
                # to get proper validation errors.
                return HttpResponse('Make sure all fields are entered and valid.')
            return redirect('/contact')
        else:
            return HttpResponse("""Your form is wrong, reload on <a href="{{url : 'index'}}">reload</a>""")

    return render(request, "contact.html", context)


class EventPage(TemplateView):
    template_name = 'events.html'





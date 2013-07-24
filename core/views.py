#encoding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from forms import ContactForm

class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_staff
        return context

def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            context['success'] = True
    else:        
        form = ContactForm()
    context['form'] = form
    return render(request, 'contact.html', context)
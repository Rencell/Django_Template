from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

class Mixin:
    def get_context_data(self, **kwargs):
        
        data = super().get_context_data(**kwargs)
        
        data['active_home'] = self.request.path == '/'
        data['active_settings'] = self.request.path == '/settings/'
        data['active_services'] = self.request.path == '/services/'
        data['active_contacts'] = self.request.path == '/contacts/'
        return data


class index(Mixin, TemplateView):
    template_name = 'app/Home.html'

class Settings(Mixin, TemplateView):
    template_name = 'app/Settings.html'
    
class Services(Mixin, TemplateView):
    template_name = 'app/Services.html'

class Contact(Mixin, TemplateView):
    template_name = 'app/Contact.html'
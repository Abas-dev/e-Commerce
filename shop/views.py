#in this application, i will be using classbase views for majority or all of the views 

from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

class AboutUsPageView(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'    

class ContactUsPageView(LoginRequiredMixin,TemplateView):
    template_name = 'contact.html'

class ProductPageView(LoginRequiredMixin,TemplateView):
    template_name = 'product.html'

class SingleProductPageView(LoginRequiredMixin,TemplateView):
    template_name = 'singleProduct.html'
    
       

    
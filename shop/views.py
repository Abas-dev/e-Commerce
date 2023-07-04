#in this application, i will be using classbase views for majority or all of the views 

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutUsPageView(TemplateView):
    template_name = 'about.html'    

class ContactUsPageView(TemplateView):
    template_name = 'contact.html'

class ProductPageView(TemplateView):
    template_name = 'product.html'

class SingleProductPageView(TemplateView):
    template_name = 'singleProduct.html'
    
       

    
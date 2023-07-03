#in this application, i will be using classbase views for majority or all of the views 

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'
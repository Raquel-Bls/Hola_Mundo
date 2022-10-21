from django.views import generic
from django.views.generic import TemplateView

# Create your views here.


class homePageview(TemplateView):
    template_name = 'home.html'

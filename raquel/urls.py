from django.urls import path
from .views import homePageview

urlpatterns = [
    path('', homePageview.as_view(), name='home'),
]

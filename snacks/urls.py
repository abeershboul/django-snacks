
from django.urls import path
from .views import Home_page ,About_page

urlpatterns = [
    path('', Home_page.as_view(),name='home'),
    path('about',About_page.as_view(),name='about')
]
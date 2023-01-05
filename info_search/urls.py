from django.urls import path
from info_search.views import basic


urlpatterns = [
    path('', basic.home, name='home'),
]

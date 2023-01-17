from django.urls import path
from info_search.views import basic


urlpatterns = [
    path('', basic.home, name='home'),
    path('<str:region>/<str:purpose>', basic.search_tweets, name='search_tweets'),
]

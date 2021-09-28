from django.urls import path
from .views import *


urlpatterns = [
	path('', SearchView.as_view(), name='search'),
]
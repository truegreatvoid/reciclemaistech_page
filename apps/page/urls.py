from django.urls import path
from .views import *

app_name = 'page'

urlpatterns = [
  path('', PageView.as_view(), name='page'),
]

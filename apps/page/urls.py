from django.urls import path
from .views import *

app_name = 'page'

urlpatterns = [
  path('', PageView.as_view(), name='page'),
  path('login/', LoginView.as_view(), name='login'),
  path('sobre/', SobreView.as_view(), name='sobre'),
  path('investidor/', InvestidorView.as_view(), name='investidor'),
  path('contato/', ContatoView.as_view(), name='contato'),
  path('pedido/?checkout=1548236&plano=semente', SementeView.as_view(), name='semente'),
  path('pedido/?checkout=7846850&plano=raizes', RaizesView.as_view(), name='raizes'),
  path('pedido/?checkout=3498756&plano=floresta', FlorestaView.as_view(), name='floresta'),
]

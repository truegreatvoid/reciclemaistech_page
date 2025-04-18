from django.views.generic import (
        TemplateView
    )
from django.shortcuts import redirect

class PageView(TemplateView):
  template_name = 'page/page.html'

class SobreView(TemplateView):
  template_name = 'sobre/page.html'

class InvestidorView(TemplateView):
    template_name = 'investidor/page.html'

class ContatoView(TemplateView):
  template_name = 'contato/page.html'

class LoginView(TemplateView):
  template_name = 'login/page.html'

class SementeView(TemplateView):
  template_name = 'pedido/semente.html'

class RaizesView(TemplateView):
  template_name = 'pedido/raizes.html'

class FlorestaView(TemplateView):
  template_name = 'pedido/floresta.html'

def redirect_to_home(request, exception=None):
    return redirect('page:page')
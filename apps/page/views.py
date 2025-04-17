from django.views.generic import (
        TemplateView
    )

class PageView(TemplateView):
    template_name = 'page/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
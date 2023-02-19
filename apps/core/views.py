from django.views.generic import TemplateView
from .tasks import add

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add.delay(4, 4)
        return context
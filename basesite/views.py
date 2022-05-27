from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'base_site/landing_page.html'

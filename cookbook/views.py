from django.views.generic import TemplateView

class Homepage(TemplateView):
    template_name = 'Falcon/index.html'

class Test(TemplateView):
    template_name = 'Falcon/index.html'

class Thanks(TemplateView):
    template_name = 'Falcon/index.html'

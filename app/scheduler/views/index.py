from django.views.generic import TemplateView




class IndexView(TemplateView):
    template_name = 'scheduler/index.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = IndexService()

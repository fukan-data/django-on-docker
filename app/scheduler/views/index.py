from django.views.generic import TemplateView

from scheduler.services.task import TaskService
from scheduler.forms.index import IndexForm

import logging

logger = logging.getLogger(__name__)



class IndexView(TemplateView):
    template_name = 'scheduler/index.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.service = TaskService()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['aaa'] = 'hihihihi1234'
        # ctx['form'] = IndexForm()



        logger.info("log info test!")
        return ctx

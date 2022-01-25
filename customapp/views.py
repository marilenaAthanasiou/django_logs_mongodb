import logging

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

request_logger = logging.getLogger('django.server')


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        request_logger.error('Hello Big Brother')
        return self.render_to_response(context)

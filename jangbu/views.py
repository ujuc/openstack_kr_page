from django.shortcuts import render
from django.views import View


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {'data': 'jangbu'}

        return render(request, self.template_name, context=context)

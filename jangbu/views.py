from django.shortcuts import render
from django.views import View
from django.core import serializers

from .models import Accounts


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        db_data = serializers.serialize('json', Accounts.objects.all())

        context = {'data': db_data}

        return render(request, self.template_name, context=context)

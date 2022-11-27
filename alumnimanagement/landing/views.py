from django.shortcuts import render
from django.views import View

class Index(View):
    template_name = 'landing/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

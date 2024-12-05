from django.shortcuts import render
from django.views.generic import TemplateView


# https://uguide.ru/tablica-osnovnykh-tegov-html-s-primerami
# Create your views here.
def func_view(request):
    return render(request, 'func_template.html')


class class_view(TemplateView):
    template_name = 'class_template.html'

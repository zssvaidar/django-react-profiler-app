from django.shortcuts import render
from django.views.generic import ListView

class indexView(ListView):
    template_name = 'frontend/index.html'

    def get_queryset(self):
        return
# def main(request):
#     context = {}
#     return render(request, 'profiler/main.html', context)
#

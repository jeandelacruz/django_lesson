from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import AuthorForm
from .models import Author


# Create your views here.
# Primera forma de crear una vista
# Vista basada en funciones
def index(request):
    return render(request, 'index.html')


@require_http_methods(['GET', 'POST'])
def create_author(request):
    form_class = AuthorForm

    if request.method == 'POST':
        # request.POST -> Recibimos lo que se envia del formulario
        record = form_class(request.POST)
        if record.is_valid():
            record.save()

    return render(request, 'authors/create.html', {
        'form': form_class
    })


# Vista basada en clases
# class IndexView(View):
#     # dispatch
#     def get(self, request):
#         return render(request, 'index.html')

#     def post(self, request):
#         pass

#     def put(self, request):
#         pass

#     def patch(self, request):
#         pass

#     def delete(self, request):
#         pass
class IndexView(TemplateView):
    template_name = 'index.html'


class AuthorsListView(ListView):
    model = Author
    template_name = 'authors/list.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/create.html'
    success_url = reverse_lazy('authors_list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/update.html'
    success_url = reverse_lazy('authors_list')

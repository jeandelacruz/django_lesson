from django.urls import path
from .views import IndexView, AuthorsListView, AuthorCreateView, AuthorUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='hola_mundo'),
    path('authors', AuthorsListView.as_view(), name='authors_list'),
    path('authors/create', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<pk>/update', AuthorUpdateView.as_view(), name='author_update')
]

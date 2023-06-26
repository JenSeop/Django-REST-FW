from django.urls import path, include
from .fbv_views import HelloAPI, bookAPI, booksAPI

urlpatterns = [
    path("hello/", HelloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
]
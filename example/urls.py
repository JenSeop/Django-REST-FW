from django.urls import path, include
from .fbv_views import HelloAPI, bookAPI, booksAPI
from .cbv_views import BookAPI, BooksAPI
from .mixins_views import BooksAPIMixins, BookAPIMixins

urlpatterns = [
    path("hello/", HelloAPI),
    # FBV
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
    # CBV
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
    # Mixins
    path("mixin/books/", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
]
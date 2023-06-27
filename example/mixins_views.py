from rest_framework import generics
from rest_framework import mixins
class BooksAPIMixins(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    queryset = Book.objects.all()
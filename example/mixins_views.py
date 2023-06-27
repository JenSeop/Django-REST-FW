from rest_framework import generics
from rest_framework import mixins
from .models import Book
from .serializers import BookSerializer

class BooksAPIMixins(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get(self, request,*args, **kwargs):         # GET 메소드 처리 함수
        return self.list(request, *args, **kwargs)  # mixins.ListModelMixin과 연결
    def post(self, request, *args, **kwargs):       # POST 메소드 처리 함수(1권 등록)
        return self.create(request, *args, **kwargs)# mixins.CreateModelMixin과 연결

class BookAPIMixins(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'
    # Django 기본 모델 pk가 아닌 bid를 pk로 사용중이니 lookup_field로 설정
    
    def get(self, request, *args, **kwargs):            # GET 메소드 처리 함수(1권)
        return self.retrieve(request, *args, **kwargs)  # mixins.RetrieveModelMixin과 연결
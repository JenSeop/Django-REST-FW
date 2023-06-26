from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404   # load get_object_or_404
from .models import Book                                # load Models
from .serializers import BookSerializer                 # load Serializer

@api_view(['GET'])              # GET 요청 처리 데코레이터
def HelloAPI(request):
    return Response("hello world!")

@api_view(['GET', 'POST'])          # GET/POST 요청 처리 데코레이터
def booksAPI(request):              # /book/
    if request.method == 'GET':     # GET 요청(도서 전체 정보)
        books = Book.objects.all()   # Book 모델로부터 전체 데이터 요청
        serializer = BookSerializer(books, many=True)
        # 시리얼라이저에 전체 데이터 전송 (직렬화, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK) # return Response
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        # POST 요청 데이터 시리얼라이저에 전송
        if serializer.is_valid():   # 유효 데이터 검증
            serializer.save()
            # 시리얼라이저 역직렬화 통해 save()
            # 모델 시리얼라이저 기본 create() 함수가 동작
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # Send 201 Message (Succes)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Error 400

@api_view(['GET'])
def bookAPI(request, bid):  # /book/bid/
    book = get_object_or_404(Book, bid=bid)
    # bid=id인 데이터 Book에서 수신, 없을 경우 404 Error
    serializer = BookSerializer(book)
    # 시리얼라이저에 데이터 전송(직렬화)
    return Response(serializer.data, status=status.HTTP_200_OK)
    # return Response
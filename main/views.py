from turtle import st
from main.models import AudioBook, Book, Category, Language
from .serializer import *
import datetime
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class AllBookView(ListCreateAPIView):
    queryset = Book.objects.all().order_by("-id")
    serializer_class = SerializerBook
    permission_classes = (IsAuthenticated)

    def post(self,request):
        auth = request.user
        name = request.POST['name']
        file = request.FILES['file']
        lang = Language.objects.get(id=request.POST['lang'])
        img = request.FILES['img']
        date = datetime.datetime.today()
        category = Category.objects.get(id=request.POST['category'])
        text = request.POST['text']
        book = book.objects.create(
            auth=auth,
            category=category,
            Lang=lang,
            file=file,
            img=img,
            date=date,
            name=name,
            text=text
            )
        ser = self.serializer_class(Book)
        return Response(ser.data)


class AllAudioBookView(ListCreateAPIView):
    queryset = Book.objects.all().order_by("-id")
    serializer_class = SerializerBook
    permission_classes = (IsAuthenticated)

    def post(self,request):
        auth = request.user
        name = request.POST['name']
        file = request.FILES['file']
        lang = Language.objects.get(id=request.POST['lang'])
        img = request.FILES['img']
        date = datetime.datetime.today()
        category = Category.objects.get(id=request.POST['category'])
        text = request.POST['text']
        book = book.objects.create(
            auth=auth,
            category=category,
            Lang=lang,
            file=file,
            img=img,
            date=date,
            name=name,
            text=text
            )
        ser = self.serializer_class(Book)
        return Response(ser.data)



class OneBookView(ListAPIView):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = SerializerBook
    permission_classes = (IsAuthenticated,)

    def get(self,request,pk:int):
        item = Book.objects.get(id=pk)
        serializer = self.serializer_class(item)
        data = serializer.data
        another_books = Book.objects.filter(auth=item.auth)
        another_ser = self.serializer_class(another_books, many=True)
        data['another'] = another_ser.data
        return Response(data)


class OneAudioBookView(ListAPIView):
    queryset = AudioBook.objects.all().order_by('-id')
    serializer_class = SerializerBook
    permission_classes = (IsAuthenticated,)

    def get(self,request,pk:int):
        item = AudioBook.objects.get(id=pk)
        serializer = self.serializer_class(item)
        return Response(serializer.data)


class RatingAudioBookAddView(ListAPIView):
    queryset = AudioBook.objects.all().order_by('-id')
    serializer_class = SerializerAudioBook
    permission_classes = (IsAuthenticated,)

    def post(self,request,pk):
        user = request.user
        book = AudioBook.objects.get(id=pk)
        star = request.POST['star']
        check = RatingAudioBook.objects.filter(auth=user)
        if len(check) > 0:
            check[0].star = star
            check[0].save()
            ser = self.serializer_class(check[0])
        else:
            new = RatingAudioBook.objects.create(auth=user,star=star,book=book)
            ser = self.serializer_class(new)

        return Response(ser.data)
        


class GoToReadAdd(ListCreateAPIView):
    queryset = HistoryBook.objects.all().order_by('-id')
    serializer_class = SerializerHistoryBook
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        book = request.POST['book']
        book = Book.objects.get(id=book)
        user = request.user
        hs = HistoryBook.objects.create(types=1, book=book, user=user)
        ser = self.serializer_class(hs)
        return Response(ser.data)
    def get(self,request):
        user = request.user
        data = self.serializer_class(HistoryBook.objects.filter(user=user),many=True).data
        return Response(data)


class ReadingAdd(ListCreateAPIView):
    queryset = HistoryBook.objects.all().order_by('-id')
    serializer_class = SerializerHistoryBook
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        book = request.POST['book']
        book = Book.objects.get(id=book)
        user = request.user
        hs = HistoryBook.objects.create(types=2, book=book, user=user)
        ser = self.serializer_class(hs)
        return Response(ser.data)
    def get(self,request):
        user = request.user
        data = self.serializer_class(HistoryBook.objects.filter(user=user),many=True).data
        return Response(data)

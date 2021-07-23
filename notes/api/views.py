from rest_framework import viewsets

from api.generics import BookSerializer
from main.models import Book


class BookAPIViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer

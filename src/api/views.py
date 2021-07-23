from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from api.generics import RateSerializer, PostSerializer
from main.models import Rate, Post


class RateAPIViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-id')
    serializer_class = RateSerializer
    pagination_class = PageNumberPagination


class RateAPIViewSet2(generics.GenericAPIView):
    queryset = Rate.objects.all().order_by('-id')

    def get(self, request):
        res = Rate.objects.all().order_by('-id')
        ser = RateSerializer(res, many=True)
        return Response(ser.data)


class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 3

from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import *

router = DefaultRouter()
router.register(prefix='rates', viewset=RateAPIViewSet, basename='rate')
router.register(prefix='articles', viewset=PostAPIViewSet, basename='article')

urlpatterns = [
    path('rates2/', RateAPIViewSet2.as_view(), name='rates2')
]


urlpatterns.extend(router.urls)


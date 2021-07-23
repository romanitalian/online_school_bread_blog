from rest_framework.routers import DefaultRouter

from api.views import BookAPIViewSet

app_name = 'api-book'

router = DefaultRouter()
router.register(prefix='books', viewset=BookAPIViewSet, basename='book')

urlpatterns = router.urls

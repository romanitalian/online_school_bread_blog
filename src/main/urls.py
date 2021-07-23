from django.urls import path, include
from django.views.decorators import cache
from django.views.generic import TemplateView, RedirectView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from main import views

# router = DefaultRouter()
# router.register(prefix='api/v1/rates', viewset=views.RateAPIViewSet, basename='rate')

urlpatterns = [
    # path('', views.index, name='home_page'),
    path('', TemplateView.as_view(template_name='main/index.html'), name='home_page'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/imgs/favicon/favicon.ico')),
    path('about/', views.about, name='about'),

    path('posts/', views.posts_all, name='posts_all'),
    path('posts/list/', views.PostsListView.as_view(), name='posts_list'),
    # path('posts/list/', views.PostsListView.as_view(), name='posts_list'),
    path('posts/list/csv', views.PostCSV.as_view(), name='posts_list_csv'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:post_id>/', views.post_show, name='post_show'),
    path('post/update/<int:post_id>/', views.post_update, name='post_update'),

    path('authors/new/', views.authors_new, name='authors_new'),
    path('authors/all/', views.authors_all, name='authors_all'),
    path('author/subscribe/', views.author_subscribe, name='author_subscribe'),
    path('author/subscribers/all/', views.author_subscribers_all, name='author_subscribers_all'),

    path('books/all/', views.books_all, name='books_all'),
    path('books/list/', views.BooksListView.as_view(), name='books_list'),

    path('api/posts/', views.json_posts, name='json_data'),
    path('api/post/<int:post_id>/', views.api_post_show, name='api_post_show'),
    path('api/subscribe/', views.api_author_subscribe, name='api_subscribe'),
    path('api/subscribers/all/', views.api_subscribers_all, name='api_subscribers_all'),
    path('api/authors/all/', views.api_authors_all, name='api_authors_all'),
    path('api/authors/new/', views.api_authors_new, name='api_authors_new'),

    path('slow/', views.slow, name='slow'),

    path('contact-us/create/', views.ContactUsView.as_view(), name='contact-us-create'),

    # API
    # path('api/v1/rates/', views.RateListAPIView.as_view(), name='api-rates'),
    # path('api/v1/rates/<int:pk>/', views.RateAPIView.as_view(), name='api-rate')

    path('api/v1/', include('api.urls')),

    path('posts-page/', TemplateView.as_view(template_name='main/posts_page.html'), name='posts-page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += router.urls

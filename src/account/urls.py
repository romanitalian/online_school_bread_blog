from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('my-profile/', views.MyProfile.as_view(), name='my_profile'),
    path('my-profile/ava/create/', views.AvaCreate.as_view(), name='my_profile_ava_create'),
    path('my-profile/ava/list/', views.AvaList.as_view(), name='my_profile_ava_list'),
]

from django.urls import path
from blog.views import RegistrationListCreateAPIView, BannerListCreateAPIView

urlpatterns = [
    path('api/register/', RegistrationListCreateAPIView.as_view(), name='registration_list_create'),
    path('api/banner/', BannerListCreateAPIView.as_view(), name='banner_list_create'),

]
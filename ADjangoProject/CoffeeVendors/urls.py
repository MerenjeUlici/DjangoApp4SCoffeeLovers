from django.urls import path
from . import views

urlpatterns = [
    path('', views.VendorsList.as_view(), name='vendors-list'),
    path('vendor/<int:pk>', views.VendorDetail.as_view(), name='vendors-by-id')

]

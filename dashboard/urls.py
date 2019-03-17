from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kembali/<int:pk>/', views.barang_kembali, name='barang_kembali'),
    path('hapus/<int:pk>/', views.hapus_list, name='hapus_list'),
]
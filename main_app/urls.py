from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('allrats/', views.rats_index, name='index'),
    path('rats/<int:rat_id>/', views.rats_detail, name='detail'),
    path('rats/create/', views.RatCreate.as_view(), name='rats_create'),
    path('rats/<int:pk>/update/', views.RatUpdate.as_view(), name='rats_update'),
    path('rats/<int:pk>/delete/', views.RatDelete.as_view(), name='rats_delete'),
]
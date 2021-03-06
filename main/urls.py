from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    path('', views.index),
    path('soja/', views.SojaList.as_view()),
    path('soja/<int:pk>/', views.SojaDetail.as_view()),
    path('milho/', views.MilhoList.as_view()),
    path('milho/<int:pk>/', views.MilhoDetail.as_view()),
    path('cafe/', views.CafeList.as_view()),
    path('cafe/<int:pk>/', views.CafeDetail.as_view()),
    path('cafe/arabica/', views.CafeArabicaList.as_view()),
    path('cafe/conillon/', views.CafeConillonList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

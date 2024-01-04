from django.urls import path
from .views import TranslationList, TranslationDetail

urlpatterns = [
    path('translations/', TranslationList.as_view(), name='translation-list'),
    path('translations/<int:pk>/', TranslationDetail.as_view(), name='translation-detail'),
]
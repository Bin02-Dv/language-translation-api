from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Translation
from .serializers import TranslationSerializer
from googletrans import Translator

class TranslationList(generics.ListCreateAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    def perform_create(self, serializer):
        source_text = serializer.validated_data['source_text']
        source_language = serializer.validated_data.get('source_language', 'en')
        target_language = serializer.validated_data.get('target_language', 'en')

        translator = Translator()
        translated_text = translator.translate(source_text, src=source_language, dest=target_language).text

        serializer.save(translated_text=translated_text)

class TranslationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer


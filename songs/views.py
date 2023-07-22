from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from albums.models import Album


class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = songs = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs["pk"])
        serializer.save(album=album)

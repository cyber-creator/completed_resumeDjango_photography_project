from rest_framework import viewsets
# Create your views here.

from .permissions import IsAuthorOrReadOnly
from apiphoto.serializers import PhotoSerializer, PhotoCategorySerializer
from album.models import Photo, Category


class PhotoAPIViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoCategoryAPIViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = PhotoCategorySerializer

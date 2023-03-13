from rest_framework import serializers
from album.models import Photo, Category


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('title', 'photo', 'category')


class PhotoCategorySerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ('id', 'name',)

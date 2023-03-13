from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register('category', views.PhotoCategoryAPIViewSets, basename='category_api')
router.register('', views.PhotoAPIViewSets, basename='photo_api')

urlpatterns = router.urls

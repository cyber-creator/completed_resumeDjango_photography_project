from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('portfolio', views.PortfolioPageView.as_view(), name='portfolio'),
    path('categories', views.ServicesPageView.as_view(), name='categories'),
    path('contacts', views.ContactsPageView.as_view(), name='contacts'),
    path('success', views.SuccessView.as_view(), name='success'),
    path("<slug:slug>/", views.AlbumCategory.as_view(), name='album_category'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

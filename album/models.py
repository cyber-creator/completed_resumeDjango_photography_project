from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('album_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField("Poster", upload_to="photo/")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="category")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    text = models.TextField(max_length=5000)

    def __str__(self):
        return f'{self.name} {self.phone}'


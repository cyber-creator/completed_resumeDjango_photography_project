from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View
from .models import Category, Photo
from album.forms import PostForm


class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class PortfolioPageView(ListView):
    template_name = 'portfolio.html'
    queryset = Photo.objects.all()
    context_object_name = "photos_to_display"
    paginate_by = 12


class ServicesPageView(ListView):
    template_name = 'services.html'
    model = Category
    context_object_name = "category_to_display"
    paginate_by = 6


class AlbumCategory(ListView):
    model = Photo
    template_name = "portfolio.html"
    context_object_name = "photos_to_display"
    paginate_by = 12

    def get_queryset(self, *args, **kwargs):
        service_pk = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Photo.objects.filter(category=service_pk.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_pk = get_object_or_404(Category, slug=self.kwargs['slug'])
        context['category_name'] = service_pk
        return context


class ContactsPageView(View):
    template_name = 'contacts.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/success")
        return redirect('portfolio')


class SuccessView(TemplateView):
    template_name = 'successForm.html'

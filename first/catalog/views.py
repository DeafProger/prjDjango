from django.views.generic import TemplateView, ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from .models import Product, Blog


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product


class ContactsView(TemplateView):
    template_name = 'contact.html'


class BlogListView(ListView):
    template_name = 'blog_list.html'
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """выводит только опубликованные блоги"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    template_name = 'blog_form.html'
    model = Blog
    fields = ('title', 'content', 'picture')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = Blog


    def get_object(self, queryset=None):
        """Cчетчик просмотров блога"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'picture')
    template_name = 'blog_form.html'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    template_name = 'blog_delete.html'
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')

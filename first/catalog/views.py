from django.views.generic import TemplateView, ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from .forms import ProductForm, VersionForm
from .models import Product, Version
from users.models import User


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'product_list.html'
    model = Product

    def get_context_data(self, **kwargs):
        """Метод для вывода названия версии если она активна"""
        context_data = super().get_context_data(**kwargs)
        version_dict = {}
        # Запускаю цикл по моделям Product и сразу запускаю цикл по моделям Version, далее алгоритм проверят что модель
        # Version активная и если он видит что она привязана к продукту, то добавляет в словарь номер продукта и его
        # активную версию
        for product in Product.objects.all():
            for version in Version.objects.all():
                if version.is_version_active:
                    if version.product_id == int(product.pk):
                        version_dict[version.product_id] = version.version_name
        context_data['versions'] = version_dict
        return context_data


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'product_detail.html'
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'product_form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.owner = self.request.user  # new line
            new_product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product_form.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product_delete.html'
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsView(TemplateView):
    template_name = 'contact.html'

'''
            if product.owner != self.request.user:
                #context_data.pop(product)
                print(context_data['product_list'])
                print(context_data['object_list'])
'''
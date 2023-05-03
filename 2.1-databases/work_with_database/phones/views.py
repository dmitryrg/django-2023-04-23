from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    _phones = Phone.objects.all()
    phones = [
        {'name': phone.name, 'price': phone.price, 'image': phone.image, 'slug': phone.slug}
        for phone in _phones
    ]

    def sort_func():
        if sort == 'name':
            return lambda x: x['name']
        if sort == 'min_price':
            return lambda x: x['price']
        if sort == 'max_price':
            return lambda x: -x['price']
    # лучше сортировать запросом к базе, но пока не понятно как
    context = {'phones': sorted(phones, key=sort_func())}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

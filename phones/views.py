from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '-name')
    phones = Phone.objects.all().order_by(sort)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.all()
    for choice_phone in phones:
        if choice_phone.slug == slug:
            phone = choice_phone
            context = {'phone': phone}
            return render(request, template, context)

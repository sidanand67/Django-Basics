from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import ProductForm, UpdateForm
from .models import ProductModel

# Create your views here.
def index(request):
    my_form = ProductForm(request.POST or None)
    context = {
        'form': my_form,
    }
    if request.method == "POST":
        if my_form.is_valid():
            print('Pass')
            my_form.save()
            return redirect('product:result')
        else:
            my_form = ProductForm()

    return render(request, 'product/index.html', context)


def update(request, pk):
    obj = get_object_or_404(ProductModel, pk=pk)
    update_form = UpdateForm(instance=obj)
    if request.method == "POST":
        update_form = UpdateForm(request.POST, instance=obj)
        if update_form.is_valid():
            print('updated')
            update_form.save()
            return redirect(reverse('product:result'))

    return render(request, 'product/update.html', {'form':update_form,})


def delete(request, pk):
    obj = get_object_or_404(ProductModel, pk=pk)
    if request.method == "POST":
        print('deleted')
        obj.delete()
        return redirect(reverse('product:result'))
    return render(request, 'product/delete.html', {})


def result(request):
    data = ProductModel.objects.all().order_by('-price')
    context = {
        "data": data,
    }
    return render(request, 'product/result.html', context)

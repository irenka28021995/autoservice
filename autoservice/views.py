from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView

from .form import ClientModelForm
from .models import Client


def index(request):
    return render(request, 'index.html')


def client_orders(request):
    client = Client.objects.all()
    return render(request, 'client_orders.html', {'title': 'Заявки клиентов', 'clients': client})


def contact(request):
    return render(request, 'contact.html')


def create_order(request):
    form = ClientModelForm()
    if request.method == 'POST':
        form = ClientModelForm(request.POST)
        if form.is_valid():
            task = Client(
                ClientName=form.cleaned_data['ClientName'],
                ClientPhone=form.cleaned_data['ClientPhone'],
                ClientCar=form.cleaned_data['ClientCar'],
            )
            task.save()
            return redirect('orders')

    context = {
        'form': form,
    }
    print(context)
    return render(request, 'create_order.html', context)


class ClientUpdateApi(UpdateView):
    form_class = ClientModelForm
    model = Client
    template_name = 'update_order.html'


class ClientDeleteApi(DeleteView):
    model = Client
    success_url = '/client_orders/'


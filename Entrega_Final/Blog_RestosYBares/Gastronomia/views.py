from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import Http404
# Redireccion
from django.urls import reverse_lazy
# Auth
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
# Create your views here.


def Index(request): 
    return render(request, 'Gastronomia/index.html')

def Pages(request):
    return render(request, 'Gastronomia/pages.html')

class RegistroView(CreateView):

    form_class = RegistroForm
    success_url = reverse_lazy('Home')
    template_name = 'Gastronomia/registro.html'

class UserLoginView(LoginView):
    template_name = 'Gastronomia/login.html'

class UserLogoutView(LogoutView):
    template_name = 'Gastronomia/logout.html'

def AboutMe(request): 
    return render(request, 'Gastronomia/about.html')

def editar_usuario(request):
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = EditarUsuarioForm(instance=request.user)

    return render(request, 'Gastronomia/editar_usuario.html', {"form": form})

def upload_resto(request):

    if request.method == 'POST':
        form = RestaurantesForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Gastronomia/index.html')
    else:
        form = RestaurantesForm

    return render(request, 'Gastronomia/upload_resto.html', {'form': form})

def upload_bar(request):
    if request.method == 'POST':
        form = BaresForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Gastronomia/index.html')
    else:
        form = BaresForm

    return render(request, 'Gastronomia/upload_bar.html', {'form': form})


class MostrarRestauranteList(ListView):
    model = Restaurantes
    template_name = 'Gastronomia/mostrar_resto.html'

class RestoDetailView(DetailView):

    model = Restaurantes
    template_name = 'Gastronomia/resto_detalle.html'

class RestoUpdateView(UpdateView):

    model = Restaurantes
    success_url = '/mostrar_restos'
    fields = '__all__'
    template_name = 'Gastronomia/edit_resto.html'

class RestoDeleteView(DeleteView):

    model = Restaurantes
    success_url = '/mostrar_restos'


class MostrarBaresList(ListView):
    model = Bares
    template_name = 'Gastronomia/mostrar_bares.html'

class BaresDetailView(DetailView):

    model = Bares
    template_name = 'Gastronomia/bares_detalle.html'

class BaresUpdateView(UpdateView):

    model = Bares
    success_url = '/mostrar_bares'
    fields = '__all__'
    template_name = 'Gastronomia/edit_bar.html'

class BaresDeleteView(DeleteView):

    model = Bares
    success_url = '/mostrar_bares'
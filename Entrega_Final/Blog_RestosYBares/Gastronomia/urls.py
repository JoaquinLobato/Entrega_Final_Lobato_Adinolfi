from django.urls import path
from Gastronomia import views

urlpatterns = [
    path('', views.Index, name = 'Home'),
    path('pages/', views.Pages, name='Pages'),
    path('registro/', views.RegistroView.as_view(), name='Registro'),
    path('login/', views.UserLoginView.as_view(), name='Login'),
    path('logout/', views.UserLogoutView.as_view(), name='Logout'),
    path('about/', views.AboutMe, name='About Me'),
    path('editar_usuario/', views.editar_usuario, name='Editar Usuario'),
    path('upload_rest/', views.upload_resto, name='Upload Resto'),
    path('upload_bar/', views.upload_bar, name='Upload Bar'),
    path('mostrar_restos/', views.MostrarRestauranteList.as_view(), name='Ver Restaurantes'),
    path('resto_detalle/<pk>', views.RestoDetailView.as_view(), name='Resto Detalle'),
    path('resto_edit/<pk>', views.RestoUpdateView.as_view(), name='Edit Resto'),
    path('resto_delete/<pk>', views.RestoDeleteView.as_view(), name='Delete Resto'),
    path('mostrar_bares/', views.MostrarBaresList.as_view(), name='Ver Bares'),
    path('bares_detalle/<pk>', views.BaresDetailView.as_view(), name='Bar Detalle'),
    path('edit_bar/<pk>', views.BaresUpdateView.as_view(), name='Edit Bar'),
    path('bar_delete/<pk>', views.BaresDeleteView.as_view(), name='Delete Bar'),
    
]

# Entrega Final Programacion con Python: Blog de Bares y Restaurantes

Joaquin Lobato Adinolfi, comision 34635. Proyecto similar a un blog de recomendaciones de tanto bares como restaurantes.

## Instalacion

El proyecto puede ser instalado via clonacion de git:
```sh
git clone https://github.com/JoaquinLobato/Entrega_Final_Lobato_Adinolfi.git
```
O mediante la descarga del zip:
```sh 
Ir a https://github.com/JoaquinLobato/Entrega_Final_Lobato_Adinolfi.git
Clickear en 'code' y luego 'Download Zip'
```
Ya con el proyecto clonado o descargado, para poder correr el servidor, se deberan crear un virtual enviroment desde la consola: 

```sh
python -m venv (segudio del nombre que se le quiera asignar al ambiente virtual)
```

Y luego instalar Django:
```sh 
pip install django
```

Una vez intalado todo ello, y asegurarnos de que el interpretador de Python sea 3.9 en adelante, nos posicionamos sobre la carpeta /Blog_RestosYBares/ que contiene el archivo manage.py y con el siguiente codigo se podra correr el servidor y la pagina:
```sh
python manage.py runserver
```

Para el proyecto de ultilizo:

🛠️ Django

🛠️ Boostrap

🛠️ HTML

🛠️ CSS

## Sobre el Codigo

La aplicacion principal se llama 'Gastronomia'. Dentro de ella se encuntran los principales modelos en models.py con las clases: Restaurantes y Bares. Ambos tienen los mismos atributos:
```sh
- Nombre: Para designar el nombre del local
- Especialidad: Para mostrar en que se destaca el establecimiento
- Locacion: Para saber donde se encuentra el local 
- Horario de Apertura: Informar el horario en el que abre
- Horario de Cierre: Informar el horario en que cierra
- Breve Descripcion: Se busca informar al usuario que encontrarara en el local mas alla de la especialidad
- Imagen: Una imagen del establecimiento
```
Estos modelos sirven tanto de formulario para ingresar nuevos restaurantes y/o bares como ver los que ya estan subidos para encontrar nuevas recomendaciones. Estos posteos pueden ser actualizados en el caso en que alguna informacion sea erronea o eliminados.

Tambien, el codigo cuenta con una estructura de creacion, edicion y registro de usuario. Esta fue realizada completamente en Django/Python. Solo podran realizar cambios o subir retaurantes los usuarios que tengan una cuenta registrada. A su vez, como cualquier proyecto en Django, existe el admin que puede ser controlado con un usuario que tenga los permisos. Se puede crear uno con el codigo:
```sh
python manage.py createsuperuser
```
## Sobre la pagina y su funcionalidad

La pagina se abre en '/' y muestra cuenta con botones que permiten iniciar sesion o registrarse en la parte superior o navbar. Cuenta con un boton que redirige a 'pages/' donde se pueden encontrar los restaurantes y/o bares cargados. Tambien cuenta con un boton en el footer que lleva hacia la pagina 'About me/'.

Una vez iniciada una sesion, el usuario puede ver dos botones nuevos: "Subir restaurante" y "Subir bar". Ellos, lo redigiran a una pagina con un formulario el cual podra cargar con los datos del local que el quiera recomendar, utilizando como modelo las clases Restaurantes y Bares antes explicadas. A su vez, tendra la posibilidad ahora de, en las paginas donde se muestran estos locales cargados, poder actualizar la informacion y/o eliminar el posteo.






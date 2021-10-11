"""laTiendaVitual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from laTiendaVitual import views as local_views
from categorias.views import indexCategoria, createCategoria, editCategoria
from productos.views import indexProductos, createProducto, editProducto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', local_views.presentacion, name='presentacion'),

    # Urls para categorias
    path('categorias/', indexCategoria, name='indexCate'),
    path('categorias/create', createCategoria, name='createCate'),
    path('categorias/edit/<int:id>/', editCategoria, name='editCate'),
    # Urls para productos
    path('productos/', indexProductos, name='indexPro'),
    path('productos/create', createProducto, name='createPro'),
    path('productos/edit/<int:id>/', editProducto, name='editPro'),
]

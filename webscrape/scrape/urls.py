from django.urls import path

from . import views

#different views we have in this file
urlpatterns = [
    path("<int:id>", views.index, name='index'),
    path("",views.home, name="home"), #home page
    path("home/",views.home,name="home"),
    path("create/",views.create,name="create"),
    path("view/",views.view,name="view"),
]

from django.urls import path
from .import views

app_name = 'ManagementApp'

urlpatterns = [
    path('managementPage/',views.managementPage),
    path('managementPagetwo/<int:id>/',views.managementPagetwo,name='managementPagetwo'),
    path('signup/',views.signup),
    path('signin/',views.signin),
    path('signout/',views.signout),
    path('restro/',views.viewfood),
    path('deletefood/<int:id>/',views.deletefood,name='deletefood'),
    path('viewbar/',views.viewdrink),
    path('deletedrink/<int:id>/',views.deletedrink),
    path('viewfitness/',views.viewfitnessplan),
    path('deletefitnessplan/<int:id>/',views.deletefitnessplan),
    path('viewRooms/',views.viewroom),
    path('deleteroom/<int:id>/',views.deleteroom),
    path('order/',views.order),
    path('addCategory/',views.addnew),
    path('addroomtype/',views.addroomtype),
    path('addroom/',views.addroom),
    path('addfood/',views.addfood),
    path('adddrink/',views.adddrink),
    path('addfitness/',views.addfitness),
    path('updateRoomStatus/<int:id>/',views.updateRoomStatus)
]

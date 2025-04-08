from django.urls import path
from .import views
urlpatterns = [
    path('',views.Homepage,name='home'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('studentmarks',views.Entermarks,name='studentmarks'),
    path('studentmarks/api/',views.Students_list_create),
    path('students/delete/<pk:pk>/',views.Students_update_delete),
]
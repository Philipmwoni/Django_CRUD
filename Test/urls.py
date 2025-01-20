from django.urls import path
from.import views
urlpatterns = [
    path('',views.Homepage,name='home'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
]
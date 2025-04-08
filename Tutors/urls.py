from django.urls import path
from . import views

urlpatterns = [
    path('api/tutors', views.tutor_list),
    path('api/tutors/delete/<pk:pk>', views.tutor_detail),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('animal_list.html', views.animal_list, name='animal_list'),
    path('animal_list_et_detail.html', views.animal_list_et_detail, name='animal_list_et_detail'),
    path('animal/<str:id_animal>/', views.animal_detail, name='animal_detail'),
    # path('animal/<str:id_animal>/?<str:message>', views.animal_detail, name='animal_detail_mes'),
]
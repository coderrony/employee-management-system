
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('all_emp', views.all_emp, name='all_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('update_emp', views.update_emp, name='update_emp'),
    path('update-single_employee/<int:pk>', views.single_update,
         name='single_update'),


    path('remove-single_employee/<int:pk>', views.remove_single_emp,
         name='remove_single_emp'),

]

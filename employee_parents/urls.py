from django.urls import path

from . import views

app_name = 'employee_parents'

urlpatterns = [
    path('', views.parent_list, name='parent_list'),
    path('add/', views.parent_form, name='parent_add'),
    path('<int:pk>/', views.parent_detail, name='parent_detail'),
    path('<int:pk>/edit/', views.parent_form, name='parent_edit'),
    path('<int:pk>/delete/', views.parent_delete, name='parent_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
	path('create/', views.add_pass, name='add-items'),
	path('all/', views.view_pass, name='view_items'),
	path('update/<int:pk>/', views.update_pass, name='update-items'),
	path('user/<int:pk>/delete/', views.delete_pass, name='delete-items'),
	
]

from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('insert', views.insertData, name="insertData"),
    path('update/<int:id>', views.updateData, name="updateData"),
    path('delete/<int:id>', views.deleteData, name="deleteData"),
]

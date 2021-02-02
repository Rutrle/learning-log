
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index_view,name='index'),
    path('new/', views.create_view,name='new'),
    path('edit/<int:blog_id>/', views.edit_view,name='edit'),
]

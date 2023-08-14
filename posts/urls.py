from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # maps to the post_list view
    # maps to the post_detail view
    path('<int:pk>/', views.post_detail, name='post_detail'),
]

from django.urls import path
from . import views # views from this folder, hence the dot.

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
]
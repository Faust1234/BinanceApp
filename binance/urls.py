from django.urls import path
from . import views



urlpatterns = (
    # path('', views.index),
    path('', views.HomeListView.as_view()),
    # path("information/<int:id>", views.information_page),
    path("information/<int:pk>", views.HomeDetailView.as_view()),
    path('edit-page', views.edit_page),


)

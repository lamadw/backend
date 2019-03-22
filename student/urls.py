from django.urls import path
from . import views

urlpatterns = [
    path('rule/', views.StudentListCreate.as_view() ),
    path('rule/<pk>', views.StudentRetrive.as_view() ),
]
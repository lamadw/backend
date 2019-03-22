from django.urls import path
from . import views

urlpatterns = [
    path('instructurerequest/', views.InstructureListCreate.as_view() ),
    path('instructurerequest/<pk>', views.InstructureUpdteRetrive.as_view() ),
    path('instructureproved/', views.provedListCreate.as_view() ),
    path('instructureproved/<pk>', views.provedUpdteRetrive.as_view() ),
]
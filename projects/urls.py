from django.urls import path
from . import views

urlpatterns = [
    path('project/',views.ProjectListCreate.as_view() ),
    path('project/<pk>',views.ProjectUpdateRetreiveDestroy.as_view() ),
    path('project/<pk>/file',views.FileListCreate.as_view() ),
    path('project/<pk>/file/<id>',views.FileUpdateRetreiveDestroy.as_view() ),

]
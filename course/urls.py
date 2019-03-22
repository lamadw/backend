from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.CourseListCreate.as_view() ),
    path('course/<pk>', views.CourseUpdateRetreiveDestroy.as_view() ),
      path('studentincourse/', views.studentincourseListCreate.as_view() ),
    path('studentincourse/<pk>', views.studentincourseUpdateRetreiveDestroy.as_view() ),
      path('hwincourse/', views.hwincourseListCreate.as_view() ),
    path('hwincourse/<pk>', views.hwincourseSerializerUpdateRetreiveDestroy.as_view() ),
      path('courseinstructure/', views.courseinstructureListCreate.as_view() ),
    path('courseinstructure/<pk>', views.courseinstructureUpdateRetreiveDestroy.as_view() ),
]
from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import StudentList, StudentListUpdate ,List


router = DefaultRouter()
router.register(r'list',List)

urlpatterns = [
    path('student/', StudentList.as_view(), name='StudentList'),
    
    path('student/<int:pk>/', StudentListUpdate.as_view(), name='StudentListUpdtae'),
    
    path('', include(router.urls))
]

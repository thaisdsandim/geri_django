from django.urls import path
from .views import UnitList, UnitDetail

urlpatterns = [
    path('unit/', UnitList.as_view(), name='unit-list'),
    path('unit/<int:pk>/', UnitDetail.as_view(), name='unit-detail'),
]

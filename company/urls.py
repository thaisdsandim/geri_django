from django.urls import path
from .views import CompanyList, CompanyDetail

urlpatterns = [
    path('company/', CompanyList.as_view(), name='company-list'),
    path('company/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
]
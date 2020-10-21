from django.urls import path

from . import views

urlpatterns = [
    path('legal_notice_page/', views.legal_notice, name='legal_notice_page'),
    ]

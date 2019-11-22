from django.urls import path
from django.views.generic import TemplateView
from os_client import views

urlpatterns = [
path('os_client/', TemplateView.as_view(template_name=("os_client_template/os_client_home.html"))),
path('os_client_detail_save/', views.os_client_detail_save),
path('os_client_login_check/', views.os_client_login_check),
path('os_client_otp_check/', views.os_client_otp_check),
path('os_client_view_properties/', views.os_client_view_properties),
path('os_client_property_block/', views.os_client_property_block),
path('os_client_blocked_properties/', views.os_client_blocked_properties),
path('os_client_unblock_property/', views.os_client_unblock_property),
path('os_client_home/', views.os_client_home),
path('os_client_welcome_home/', views.os_client_welcome_home),
path('os_client_register/',TemplateView.as_view(template_name='os_client_template/os_client_register.html')),
]


from re import template
from django.urls import path
from django.views.generic.base import TemplateView
from os_admin import views

urlpatterns = [
path('os_admin/', TemplateView.as_view(template_name="os_admin_template/os_admin_home.html")),
path('os_admin_otp/', TemplateView.as_view(template_name=("os_admin_template/os_admin_otp.html"))),
path('os_admin_login_check/', views.os_admin_login_check),
path('os_admin_welcome_page/', views.os_admin_welcome_page),
path('os_admin_agent_registration/', views.os_admin_agent_registration),
path('os_admin_logout/', views.os_admin_logout),
path('os_admin_save_agent/', views.os_admin_save_agent),
path('os_admin_agent_delete/', views.os_admin_agent_delete),
path('os_admin_welcome_home/', views.os_admin_welcome_home),
path('os_admin_view_property/',views.os_admin_view_property),
path('os_admin_view_client/',views.os_admin_view_client),
path('os_admin_view_client_delete/', views.os_admin_view_client_delete),
path('os_admin_about_us/', views.os_admin_about_us),
path('os_admin_contactus/', TemplateView.as_view(template_name='os_admin_template/os_admin_contactus.html')),
path('os_admin_agent_update/', views.os_admin_agent_update)
]

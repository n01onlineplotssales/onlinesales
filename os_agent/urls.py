from re import template
from django.urls import path
from django.views.generic.base import TemplateView
from os_agent import views

urlpatterns = [
path('os_agent/', TemplateView.as_view(template_name=("os_agent_template/os_agent_home.html"))),
path('os_agent_login_check/', views.os_agent_login_check),
path('os_agent_welcome_home_page/', views.os_agent_welcome_home_page),
path('os_agent_new_properties/', views.os_agent_new_properties),
path('os_agent_save_property/', views.os_agent_save_property),
path('os_agent_property_delete/', views.os_agent_property_delete),
path('os_agent_block_property/', views.os_agent_block_property),
path('os_agent_sold_property/', views.os_agent_sold_property),
path('os_agent_logout/', views.os_agent_logout),
path('os_agent_property_update/', views.os_agent_property_update),
path('os_agent_property_update_confirm/', views.os_agent_property_update_confirm),
path('os_agent_view_sold_property/', views.os_agent_view_sold_property),
path('os_agent_welcome_page/', views.os_agent_welcome_page),
path('os_agent_sold_delete/',views.os_agent_sold_delete)
]
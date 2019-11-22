from django.urls import path
from django.views.generic import TemplateView

from os_main import views

urlpatterns = [
    path('', TemplateView.as_view(template_name=("os_main_template/os_main_home.html"))),
# path('os_main_title/', TemplateView.as_view(template_name=("os_main_template/main_title.html"))),
# path('os_main_menu/', TemplateView.as_view(template_name=("os_main_template/main_menu.html"))),
# path('os_main_footer/', TemplateView.as_view(template_name=("os_main_template/main_footer.html")))
    path('os_main_slider/',TemplateView.as_view(template_name=("os_main_template/slider.html"))),
    path('os_main_about_us/',TemplateView.as_view(template_name='os_main_template/os_main_about_us.html')),
    path('os_main_contactus/',TemplateView.as_view(template_name='os_main_template/os_main_contactus.html')),


]

from django.urls import path
from .views import home_page_view, project_detail_view , contact_view, about_view, education_view, services_view

# pages/urls.py
urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", about_view, name="about"), # New
    path("education/", education_view, name="education"), # New
    path("services/", services_view, name="services"), # New
    path("contact/", contact_view, name="contact"),
    path("project/<int:pk>/", project_detail_view, name="project_detail"),
]
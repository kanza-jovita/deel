from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name ="login.html"), name="login"),
    path("dash/",views.dash, name="dash"),
    path("payments/",views.payments, name="payments"),
    path("dolls/",views.dolls, name="dolls"), 
    path("procurement/",views.procurement, name="procurement"),

    path("addbaby/", views.addbaby, name="addbaby"),
    path("babiesform/", views.babiesform, name="babiesform"),
    path("read/<int:id>/", views.read, name="read"),
    path("edit/<int:id>/", views.edit, name="edit"),

    path("addsitter/", views.addsitter, name="addsitter"),
    path("sittersform/", views.sittersform, name="sittersform"),
    path("read_sitter/<int:id>/", views.read_sitter, name="read_sitter"),
    path("edit_sitter/<int:id>/", views.edit_sitter, name="edit_sitter"),
   

]

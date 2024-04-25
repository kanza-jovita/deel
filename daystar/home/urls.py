from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index, name="index"),
    #login and logout
    path("login/", auth_views.LoginView.as_view(template_name ="login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='project/index.html'),name='logout'),

    path("dash/",views.dash, name="dash"),
    path("payments/",views.payments, name="payments"),
    path("dolls/",views.dolls, name="dolls"), 
   

    #babies
    path("addbaby/", views.addbaby, name="addbaby"),
    path("babiesform/", views.babiesform, name="babiesform"),
    path("read/<int:id>/", views.read, name="read"),
    path("edit/<int:id>/", views.edit, name="edit"),

    #sitters
    path("addsitter/", views.addsitter, name="addsitter"),
    path("sittersform/", views.sittersform, name="sittersform"),
    path("read_sitter/<int:id>/", views.read_sitter, name="read_sitter"),
    path("edit_sitter/<int:id>/", views.edit_sitter, name="edit_sitter"),


    path("procurement/",views.procurement, name="procurement"),
    path('procurement/<int:product_id>',views.product_detail,name='product_detail'),

  #receipt
    path('receipt/',views.receipt,name='receipt'),
    path('receipt/<int:receipt_id>',views.receipt_detail,name='receipt_detail'),
    
  #sales
    path('issue_item/<str:pk>',views.issue_item,name='issue_item'),
    path('all_sales/',views.all_sales,name='all_sales'),

  #add to stock
    path('add_to_stock/<str:pk>',views.add_to_stock,name='add_to_stock'),

]

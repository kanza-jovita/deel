from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index, name="index"),
    path("home/",views.home, name="home"),
    path("payment/",views.payment, name="payment"),    
#login and logout
    path("login/", auth_views.LoginView.as_view(template_name ="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='project/index.html'), name='logout'),
#babies
    path("addbaby/", views.addbaby, name="addbaby"),
    path("babiesform/", views.babiesform, name="babiesform"),
    path("read/<int:id>/", views.read, name="read"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("delete_baby/<int:id>/", views.delete_baby, name="delete_baby"),
    path("search_baby/", views.search_baby, name="search_baby"),
#sitters
    path("addsitter/", views.addsitter, name="addsitter"),
    path("sittersform/", views.sittersform, name="sittersform"),
    path("read_sitter/<int:id>/", views.read_sitter, name="read_sitter"),
    path("edit_sitter/<int:id>/", views.edit_sitter, name="edit_sitter"),
    path("search_sitter/", views.search_sitter, name="search_sitter"),
#Dolls
    path('doll/', views.doll, name='doll'),
    path('dollscorner/<int:doll_id>/', views.dollcorner, name='dollcorner'),
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),
    path('all_sales/', views.all_sales, name='all_sales'),
    path('issue_item/<str:pk>', views.issue_item, name='issue_item'),
    path('receipt/', views.receipt, name='receipt'),
    path('receipt_detail/<int:receipt_id>', views.receipt_detail, name='receipt_detail'),
#arrival and departure
    path('arrival/', views.arrival, name='arrival'),
    path('departure/', views.departure, name='departure'),
    path('arrival_form/', views.arrival_form, name='arrival_form'),
    path('departure_form/', views.departure_form, name='departure_form'),
    path('arrival_form/<int:id>/', views.arrival_form, name='arrival_form'),
    path('departure_form/<int:id>/', views.departure_form, name='departure_form'),
#procurement
    path('inventory/', views.inventory, name='inventory'),
    path('add_to_stocks/<str:pk>', views.add_to_stocks, name='add_to_stocks'),
    path('all_issue_items/', views.all_issue_items, name='all_issue_items'),
    path('issue/<str:pk>',views.issue,name='issue'),
#payments
    path('paymentform/', views.paymentform, name='paymentform'),
    path('addpayment/', views.addpayment, name='addpayment'),
    path('editpayment/<int:id>/', views.editpayment, name='editpayment'),
    path('paymentlist/', views.paymentlist, name='paymentlist'),
    path('createpayment/', views.createpayment, name='createpayment'),
]

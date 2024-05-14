from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index, name="index"),
    path("home/",views.home, name="home"),    
#login and logout
    path("login/", auth_views.LoginView.as_view(template_name ="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name ="logout.html"), name="logout"),
    
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
     path("delete_sitter/<int:id>/", views.delete_sitter, name="delete_sitter"),
     
#Dolls
    path('doll/', views.doll, name='doll'),
    path('dollscorner/<int:doll_id>/', views.dollcorner, name='dollcorner'),
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),
    path('all_sales/', views.all_sales, name='all_sales'),
    path('issue_item/<str:pk>', views.issue_item, name='issue_item'),
    path('receipt/', views.receipt, name='receipt'),
    path('receipt_detail/<int:receipt_id>', views.receipt_detail, name='receipt_detail'),
#departure
    # path('arrival/', views.arrival, name='arrival'),
    # path('addarrival/', views.addarrival, name='addarrival'),
    # path('editarrival/<int:id>/', views.editarrival, name='editarrival'),
    path('departure/', views.departure, name='departure'),
    path('adddeparture/', views.adddeparture, name='adddeparture'),
    path('editdeparture/<int:id>/', views.editdeparture, name='editdeparture'),
    path('onduty/', views.onduty, name='onduty'),
    path('addonduty/', views.addonduty, name='addonduty'),
    path('editdontudy/<int:id>/', views.editonduty, name='editonduty'),
    path('delete/<int:id>/', views.delete_onduty, name='delete_onduty'),
    path('add_sitter_departure/', views.add_sitter_departure, name='add_sitter_departure'),
    path('sitter_departure/', views.sitter_departure, name='sitter_departure'),
    path('editoffduty/<int:id>/', views.editoffduty, name='editoffduty'),
     

#procurement
    path('inventory/', views.inventory, name='inventory'),
    path('add_to_stocks/<str:pk>', views.add_to_stocks, name='add_to_stocks'),
    path('all_issue_items/', views.all_issue_items, name='all_issue_items'),
    path('issue/<str:pk>',views.issue,name='issue'),
#payments
    path('paymentform/', views.payment, name='paymentform'),
    path('addpayment/', views.addpayment, name='addpayment'),
    path('editpayment/<int:id>/', views.editpayment, name='editpayment'),
    path('paymentform/', views.all_payments, name='paymentform'),
#sitterpayment
    path('add_payment/', views.add_payment, name='add_payment'),
    path('pay_list/', views.pay_list, name='pay_list'),


#assign
    path('assign_view/', views.assign_view, name='assign_view'),
    path('assign_sitter/<int:id>/', views.assign_sitter, name='assign_sitter'),


#Checkin and Checkout
    path('checkin/<int:baby_id>/', views.checkin, name='checkin'),
    path('checkout/<int:checkin_id>/', views.checkout, name='checkout'),

]



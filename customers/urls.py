from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),

    path('customers/', views.customers, name='customers'),
    path('customers_completed/', views.customers_completed, name='customers_completed'),
    path('customers/create/', views.create_customer, name='create_customer'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:customer_id>/complete/',
         views.complete_customer, name='complete_customer'),
    path('customers/<int:customer_id>/delete/', views.delete_customer, name='delete_customer'),
]
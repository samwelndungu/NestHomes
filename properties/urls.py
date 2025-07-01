from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='Home'),  # Homepage
    path('listings/', views.property_list, name='property_list'),  # Properties page
    path('buy/<int:property_id>/', views.buy_property, name='buy_property'),
    path('listings/<int:pk>/', views.property_detail, name='property_detail'),  # 👈 New detail route
    path('contact/', views.contact_view, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]


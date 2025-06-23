from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),  # Homepage
    path('listings/', views.property_list, name='property_list'),  # Properties page
    path('buy/<int:property_id>/', views.buy_property, name='buy_property'),
    path('listings/<int:pk>/', views.property_detail, name='property_detail'),  # 👈 New detail route
]


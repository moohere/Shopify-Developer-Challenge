from django.urls import path

from . import views

# The marketplace is the base application, so please visit 127.0.0.1:8000/marketplace
app_name = 'marketplace'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
]
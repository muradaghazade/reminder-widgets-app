from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    
    path('payment_process/', views.payment_process, name='payment_process' ),
]
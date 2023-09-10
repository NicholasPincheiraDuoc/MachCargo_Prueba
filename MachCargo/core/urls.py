from . import views
from django.urls import path

app_name = "CORE"

urlpatterns = [
    
    path('form', views.postFormPedido, name="post_form_pedido"),

    
   
   
]

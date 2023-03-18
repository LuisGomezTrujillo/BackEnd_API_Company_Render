from django.urls import path
from .views import companyListView, companyListView2

urlpatterns = [

    path('company/', companyListView.as_view(), name='company_list'), # ruta raiz que nos va arrojar todas las companias
    path('company/<int:id>/', companyListView.as_view(), name='company'),   
    # si quieren buscar por id. necesitan el  <int:id>, definir la variable, como entero
    # y para una palabra necesitan definirlo como un string <str>
    path('company/name/<str:name>/', companyListView2.as_view(), name='company_id'),  

]
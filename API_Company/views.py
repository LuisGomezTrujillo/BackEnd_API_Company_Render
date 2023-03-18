from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from django.views import View  # para utilizar las vistas en las rutas

from .models import company  # importamos el modelo de la base de datos
from django.http import JsonResponse  # convertir en un arvhivo Json de lectura, nuestra respuesta de la API

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json 
# Create your views here.

class companyListView(View):   # clase para poder visualizar los datos de la base de datos

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0): 
        print(id)
        if (id > 0):
            companylist = list(company.objects.filter(id=id).values())
            if len(companylist) > 0:
                datos = {'message': "Success", 'companies': companylist}
            else:
                datos = {'message': "Company not Found..."}
            return JsonResponse(datos)
            
        else:             # funcion get para obtener los datos de la base de datos
            companylist = list(company.objects.all().values())
            if(len(companylist)>0):
                datos = {'message': "Success", 'companies': companylist}
            else:
                datos = {'message': "Companies not Found..."}
            return JsonResponse(datos, safe=False)


    def post(self, request):

        datos_recibos = json.loads(request.body)
        print(datos_recibos)
        company.objects.create(name=datos_recibos['name'], email=datos_recibos['email'], website=datos_recibos['website'], fundador=datos_recibos['fundador'])
        datos = {'message': "Su nuevo dato fue guardado correctamente"}
        return JsonResponse(datos)


    def put(self, request, id):
        datos_recibos = json.loads(request.body)
        print(datos_recibos)
        companylist = list(company.objects.filter(id=id).values())
        if len(companylist) > 0 :
            company2 = company.objects.get(id=id)
            company2.name = datos_recibos['name']
            company2.email = datos_recibos['email']
            company2.website = datos_recibos['website']
            company2.fundador = datos_recibos['fundador']
            company2.save()
            datos = {'message': "La empresa ha sido actualizada de forma correcta"}
        else:
            datos = {'message': "La compania no existe..."}
        return JsonResponse(datos)


    def delete(self, request, id):
        companylist = list(company.objects.filter(id=id).values())
        if len(companylist) > 0 :
            company.objects.filter(id=id).delete()
            datos = {'message': "La empresa ha sido Eliminada de forma correcta"}
        else:
            datos = {'message': "La compania no existe..."}
        return JsonResponse(datos)


class companyListView2(View):   # clase para poder visualizar los datos de la base de datos

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, name=''): 
        if (len(name) >0):
            companylist = list(company.objects.filter(name=name).values())
            if len(companylist) > 0:
                datos = {'message': "Success", 'companies': companylist}
            else:
                datos = {'message': "Company not Found..."}
            return JsonResponse(datos)



from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from parser import parse_bp
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handler(request, recurso):
    fila = Pages.objects.filter(name=recurso)
    if request.method == "GET":
        titulares = parse_bp()
        if not fila:
            return HttpResponseNotFound("Pagina no encontrada" + titulares)
        else:
            return HttpResponse(fila[0].page + titulares)
    elif request.method == "PUT":
        if not fila:
            if recurso == "":
                fila = Pages(name=recurso, page="Pagina principal")
            else:
                fila = Pages(name=recurso, page="Pagina de " + recurso)
            fila.save()
            return HttpResponse(fila.page + titulares)
        else:
            return HttpResponse("Esta pagina ya esta almacenada")
    else:
        return HttpResponseNotFound("Metodo erroneo")
            
def update(request):
    titulares = parse_bp()
    return HttpResponse("Los titulares se han actualizado")

    

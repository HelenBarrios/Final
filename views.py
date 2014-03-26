# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.forms import ModelForm
from django.template import RequestContext 
from django.http import HttpResponseRedirect
from hoteles.models import *
from django.contrib.auth import logout

class ReservacionForm(ModelForm):
    class Meta:
        model = Reservacion
        fields = ('llegada', 'salida', 'habitacion')

def user_logout(request):
    logout(request)
    
    return HttpResponseRedirect('/')
       
def homepage(request, departamento_url='', municipio_url=''):
	
    if request.method == 'POST':
        reservacion = ReservacionForm(request.POST)
        if reservacion.is_valid():
            reservacion.save()
        else:
            return HttpResponseRedirect('/')
            
        reservacion_form = ReservacionForm()
        reservacion = Reservacion.objects.filter(user=request.user)

        param = {'titulo': titulo,
                 'url': '/reservacion',
                 'reservacion_form': reservacion_form,
                 'reservacion': reservacion,}

        return render(request, 'hoteles/reservaciones.html', param,)	
        

    titulo = u'Hoteles En Guatemala'
    descripcion = u'Busca aquí información sobre hoteles de toda la república.'
    reservacion_form = ReservacionForm()

    l = []
    if departamento_url == '':
        for dep in Departamento.objects.all():
            conteo= Hotel.objects.filter(municipio__departamento=dep).count()
            l.append('<a href="/{0}">{0}: {1} Hoteles</a>'.format(dep, conteo))
    elif len(departamento_url) > 0:
        for mun in Municipio.objects.filter(departamento__nombre=departamento_url):
            conteo= Hotel.objects.filter(municipio=mun).count()
            l.append('<a href="/{0}/{1}">{1}: {2} Hoteles</a>'.format(mun.departamento, mun, conteo,))
 #   elif len(municipio_url) > 0:
	#	for hot in Hotel.objects.filter(municipio__nombre=municipio_url):
	#		conteo= Habitacion.objects.filter(habitacion=hot)
			
            
    slideshow = Hotel.objects.all().order_by('?')[:4]

    
    
    c = RequestContext(request,
                       {'titulo': titulo,
                        'reservacion_form': reservacion_form,
                        'descripcion': descripcion,
						'lista_dept': l,
						'slideshow': slideshow},)

    return render(request, 'hoteles/homepage.html', c,)

def famosos(request):
    titulo = 'Hoteles Famosos de Guatemala'

    return render(request, 'hoteles/famosos.html', {'titulo': titulo},)
    
def reservacion(request):
    if request.method == 'POST':
        reservacion = ReservacionForm(request.POST)
        if reservacion.is_valid():
            reservacion.save()
        else:
            return HttpResponseRedirect('/')

    titulo = 'Haz tu reservacion'
    reservacion_form = ReservacionForm()
    reservacion = Reservacion.objects.all()

    param = {'titulo': titulo,
             'url': '/reservaciones',
             'reservacion_form': reservacion_form,
             'reservacion': reservacion,}

    return render(request, 'hoteles/reservacion.html', param,)

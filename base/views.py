from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View, DetailView
from .models import RedesSociales, Autor
from base.data import *
import pandas as pd
import json

# Create your views here.

def obtenerRedes():
    return RedesSociales.objects.filter(
        estado = True,
    ).latest('fecha_creacion')

def obtenerAutor():
    return Autor.objects.filter(
        estado = True,
    ).latest('fecha_creacion')

def Inicio (request):
    # resumen
    contagios = "{:,.0f}".format(total_res_wor['Contagiados'][0])
    fallecidos = "{:,.0f}".format(total_res_wor['Fallecidos'][0])
    vacunados = "{:,.0f}".format(total_res_wor['Vacunados'][0])
    fechas = "{}".format(total_res_wor['Fecha'][0])

    # Contagiados, fallecidos y vacunados

    fecha_contagios = date_cases_deaths['Fecha'].tolist()
    total_contagiados = date_cases_deaths['Total contagiados'].tolist()
    total_fallecidos = date_cases_deaths['Total fallecidos'].tolist()
    total_vacunados = date_cases_deaths['Total vacunados'].tolist()


    # 20 primeros paises

    ## contagios
    pais20contagios = Country_total_cases_deaths.sort_values('Total contagiados',ascending=False).head(20)
    N_pais20contagios = pais20contagios['Pais'].tolist()
    C_pais20contagios = pais20contagios['Total contagiados'].tolist()


    ## fallecidos
    pais20fallecidos = Country_total_cases_deaths.sort_values('Total fallecidos',ascending=False).head(20)
    N_pais20fallecidos = pais20fallecidos['Pais'].tolist()
    C_pais20fallecidos = pais20fallecidos['Total fallecidos'].tolist()

    ## vacunados
    pais20vacunados = Country_total_cases_deaths.sort_values('Total vacunados',ascending=False).head(20)
    N_pais20vacunados = pais20vacunados['Pais'].tolist()
    C_pais20vacunados = pais20vacunados['Total vacunados'].tolist()


    # Continente

    continentes = Continent_total_cases_deaths.groupby(['Continente']).sum().reset_index()
    contientesNombre = continentes['Continente'].tolist()
    continentesContagios = continentes['Total contagiados'].tolist()
    continentesFallecidos = continentes['Total fallecidos'].tolist()
    continentesVacunados = continentes['Total vacunados'].tolist()


    # Table

    
    json_records = table1.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)

    # map

    map_final_contagiados = map_cases_deaths.to_numpy().tolist()
    map_final_fallecidos = map_final_deaths.to_numpy().tolist()
    map_final_vacunados = map_final_vaccins.to_numpy().tolist()
    
    context = {

        # resumen
        'contagio': contagios,
        'fallecido': fallecidos,
        'vacunado': vacunados,
        'fecha': fechas,
        

        # No por fecha
        'fecha_contagios':fecha_contagios,
        'total_contagiados':total_contagiados,
        'total_fallecidos':total_fallecidos,
        'total_vacunados':total_vacunados,


        # 20 primeros

        ## 20 contagios
        'N_pais20contagios': N_pais20contagios,
        'C_pais20contagios': C_pais20contagios,

        ## 20 fallecidos
        'N_pais20fallecidos': N_pais20fallecidos,
        'C_pais20fallecidos': C_pais20fallecidos,

        ## 20 vacunados
        'N_pais20vacunados': N_pais20vacunados,
        'C_pais20vacunados': C_pais20vacunados,


        # Contiente
        'contientesNombre':contientesNombre,
        'continentesContagios': continentesContagios,
        'continentesFallecidos': continentesFallecidos,
        'continentesVacunados':continentesVacunados,


        # tabla
        'd': data, 

        # map
        'map_final_contagiados':map_final_contagiados,
        'map_final_fallecidos':map_final_fallecidos,
        'map_final_vacunados':map_final_vacunados,

        # Redes
        'sociales':obtenerRedes(),
        'autor':obtenerAutor(),

    }

    return render(request,'index.html',context)
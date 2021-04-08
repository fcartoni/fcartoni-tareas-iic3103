from django.shortcuts import render
from django.http import HttpResponse, Http404
import requests


def index(request):
    revisar = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes')
    codigo = revisar.status_code
    if codigo == 429:
        return render(request, 'app_tarea_1/index.html', {'error': revisar.status_code})
    else:
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes').json()
        nombres_series = []
        nombre = ''
        for i in response:
            if i['series'] != nombre:
                nombres_series.append(i['series'])
                nombre = i['series']
        return render(request, 'app_tarea_1/index.html', {'nombres_series': nombres_series})


def temporadas(request, serie):
    response = {}
    if serie == 'Breaking Bad':
        revisar = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
        codigo = revisar.status_code
        if codigo == 429:
            return render(request, 'app_tarea_1/index.html', {'error': revisar.status_code})
        else:
            response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    elif serie == 'Better Call Saul':
        revisar = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
        codigo = revisar.status_code
        if codigo == 429:
            return render(request, 'app_tarea_1/index.html', {'error': revisar.status_code})
        else:
            response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    n_temporadas = []
    actual = 0
    for i in response:
        if int(i['season']) > actual:
            n_temporadas.append(int(i['season']))
            actual = int(i['season'])
    return render(request, 'app_tarea_1/temporadas.html', {'n_temporadas': n_temporadas, 'serie': serie})


def episodios(request, serie, n_temporada):
    response = {}
    if serie == 'Breaking Bad':
        revisar = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
        codigo = revisar.status_code
        if codigo == 429:
            return render(request, 'app_tarea_1/index.html', {'error': revisar.status_code})
        else:
            response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    elif serie == 'Better Call Saul':
        revisar = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
        codigo = revisar.status_code
        if codigo == 429:
            return render(request, 'app_tarea_1/index.html', {'error': revisar.status_code})
        else:
            response = requests.get(
            'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    # else:
    #     return HttpResponse('Error 404: Esa página no existe')
    episodios_nro_nombre = []
    for i in response:
        if int(i['season']) == int(n_temporada):
            episodios_nro_nombre.append({'numero': i['episode'],'titulo': i['title'], 'serie': serie, 'n_temporada': n_temporada})
    return render(request, 'app_tarea_1/episodios.html', {'episodios_nro_nombre': episodios_nro_nombre})


def detalle_episodios(request, serie, n_temporada, n_episodio):
    response = {}
    if serie == 'Breaking Bad':
        revisar = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
        codigo = revisar.status_code
        if codigo == 429:
            return render(request, 'app_tarea_1/index.html', {'error': revisar.status_code})
        else:
            response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    elif serie == 'Better Call Saul':
        revisar = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
        codigo = revisar.status_code
        if codigo == 429:
            return render(request, 'app_tarea_1/index.html', {'error': revisar.status_code})
        else:
            response = requests.get(
            'https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    else:
        return HttpResponse('Error 404: Esa página no existe')
    detalles = []
    for i in response:
        if int(i['season']) == int(n_temporada):
            if int(i['episode']) == int(n_episodio):
                detalles.append(i)
    return render(request, 'app_tarea_1/detalle_episodios.html', {'detalles': detalles})


def personaje(request, nombre_personaje):
    new_name = nombre_personaje
    for letra in nombre_personaje:
        if letra == ' ':
            new_name = nombre_personaje.replace(letra, '+')
    revisar_1 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=' + new_name)
    codigo_1 = revisar_1.status_code
    revisar_2 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/quote?author=' + new_name)
    codigo_2 = revisar_2.status_code
    if codigo_1 == 429 or codigo_2 == 429:
        return render(request, 'app_tarea_1/index.html', {'error': 429})
    else:
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=' + new_name).json()
        quotes = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/quote?author=' + new_name).json()
        return render(request, 'app_tarea_1/personaje.html', {'response': response, 'quotes': quotes})


def buscar_personaje(request):
    if request.method == "POST":
        busqueda = request.POST['searched']
        for letra in busqueda:
            if letra == ' ':
                busqueda = busqueda.replace(letra, '+')
        resultado_por_pagina = 10
        response = {}
        i = 0
        total_personajes = []
        while resultado_por_pagina == 10:
            revisar = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=' + busqueda + '&limit=10&offset=' + str(i))
            codigo = revisar.status_code
            if codigo == 429:
                return render(request, 'app_tarea_1/index.html', {'error': 429})
            else:
                response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=' + busqueda + '&limit=10&offset=' + str(i)).json()
                resultado_por_pagina = len(response)
                for j in response:
                    total_personajes.append(j)
                i += 10
        nombre_personajes_encontrados = []
        for i in total_personajes:
            nombre_personajes_encontrados.append(i['name'])
        return render(request, 'app_tarea_1/buscar_personaje.html', {'personajes': nombre_personajes_encontrados})
    else:
        return render(request, 'app_tarea_1/buscar_personaje.html', {})


def home(request):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters').json()
    print(response)
    return render(request, 'app_tarea_1/home.html', {'response': response})

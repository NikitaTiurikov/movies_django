from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Content, Type, Genre, Registration
from .forms import AddRegistrationForm, AddLogInForm, FilterForm, SortForm

def index(request):
    movies = Content.objects.filter(type=1).order_by('-rating')[:5]
    cartoons = Content.objects.filter(type=2).order_by('-rating')[:5]
    series = Content.objects.filter(type=3).order_by('-rating')[:5]
    data = {
        'title': 'Головна',
        'movies': movies,
        'cartoons': cartoons,
        'series': series
    }
    return render(request, 'movies/index.html', data)

def selected_type(request, cat):
    filter_form = FilterForm(request.POST or None)
    sort_form = SortForm(request.POST or None)
    cat_id = Type.objects.get(slug=cat).id
    data = {
        'title': Type.objects.get(slug=cat).name,
        'filter_form': filter_form,
        'sort_form': sort_form
    }
    if request.method == 'POST':
        print(request.POST)
        req = request.POST
        if req['action'] == 'filter':
            if req['filter_by_country'] == '1':
                data['result'] = Content.objects.filter(type=cat_id, country=1)
            else:
                data['result'] = Content.objects.filter(type=cat_id, country=0)
            return render(request, 'movies/selected.html', data)
        elif req['action'] == 'sort':
            if req['sort_by'] == '1':
                data['result'] = Content.objects.filter(type=cat_id).order_by('title')
            elif req['sort_by'] == '2':
                data['result'] = Content.objects.filter(type=cat_id).order_by('-rating')

    data['result'] = Content.objects.filter(type=cat_id)

    return render(request, 'movies/selected.html', data)

def selected_genre(request, cat, genre):
    cat_id = Type.objects.get(slug=cat).id
    genre_id = Genre.objects.get(slug=genre).id
    filter_form = FilterForm(request.POST or None)
    sort_form = SortForm(request.POST or None)
    result = Content.objects.filter(type=cat_id,genre=genre_id)
    data = {
        'title': Genre.objects.get(slug=genre).name,
        'filter_form': filter_form,
        'sort_form': sort_form,
        'result': result
    }
    if request.method == 'POST':
        print(request.POST)
        req = request.POST
        if req['action'] == 'filter':
            if req['filter_by_country'] == '1':
                data['result'] = data['result'].filter(type=cat_id, country=1)
            else:
                data['result'] = data['result'].filter(type=cat_id, country=0)
            return render(request, 'movies/selected.html', data)
        elif req['action'] == 'sort':
            if req['sort_by'] == '1':
                data['result'] = data['result'].order_by('title')
            elif req['sort_by'] == '2':
                data['result'] = data['result'].order_by('-rating')
            return render(request, 'movies/selected.html', data)
    return render(request, 'movies/selected.html', data)

def selected_picture(request, pict_id):
    result = Content.objects.get(pk=pict_id)
    genre = Genre.objects.get(pk=result.genre_id).name
    data = {
        'title': result.title,
        'result': result,
        'genre': genre
    }

    return render(request, 'movies/picture.html', data)

def registration(request):
    form = AddRegistrationForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        return redirect('home')

    data = {
        'title': 'Реєстрація',
        'form' : form,
    }

    return render(request, 'movies/registration.html', data)


def login(request):
    form = AddLogInForm(request.POST or None)
    if request.method == 'POST':
        data = request.POST
        user = Registration.objects.get(login=data['login'])
        if user.pwd == data['pwd']:
            return redirect('home')
        else: return HttpResponse('Немає такого користувача')
    data = {
        'title': 'Логін',
        'form': form,
    }
    return render(request, 'movies/login.html', data)

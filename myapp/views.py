from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Players
from django.db.models.aggregates import Count, Sum
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    all_players = Players.objects.all().order_by('-id')

    paginator = Paginator(all_players, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj
    }

    return render(request, 'home.html', context)  

# ----Add player-----
def add_player(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        country = request.POST['country']
        game = request.POST['game']
        score = request.POST['score']
  
        Players.objects.create(name=name, email=email, country=country,
                                game=game, score=score)

        return JsonResponse('success', safe=False)


# ----Edit player-----
def edit_player(request, pk):
    if request.method == 'POST':

        player = Players.objects.get(id=pk)
        player.name = request.POST['name']
        player.email = request.POST['email']
        player.country = request.POST['country']
        player.game = request.POST['game']
        player.score = request.POST['score']
  
        player.save()

        return redirect('home')


# ----Delete player-----
def delete_player(request, pk):
    if request.method == 'GET':

        player = Players.objects.get(id=pk)
        player.delete()

        return JsonResponse('success', safe=False)


# ----Top players-----
def top_players(request):

    top_all_player = Players.objects.values('name', 'email', 'country').annotate(number_of_game=Count('game')).annotate(total_score=Sum('score')).order_by('-total_score')

    paginator = Paginator(top_all_player, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'top-players.html', context)
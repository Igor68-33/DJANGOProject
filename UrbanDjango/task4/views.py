from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def shop(request):
    # games_list = ['Игра первая',
    #               'Игра вторая',
    #               'Игра третья']
    # games_num = ['game' + str(x) for x in range(1, 4)]
    games = ['Atomic Heart',
             'Cyberpunk 2077']
    context = {'games': games}
    # context = dict(zip(games_num, games_list))
    return render(request, 'shop.html', context)


def basket(request):
    # games_buy = []
    games_buy = ['Atomic Heart']
    len_games_buy = len(games_buy)
    print("len_games_buy", len_games_buy)
    context = {'games_buy': games_buy,
               'len_games_buy': len_games_buy}
    return render(request, 'basket.html', context)


def menu(request):
    return render(request, 'menu.html')

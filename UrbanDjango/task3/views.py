from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def shop(request):
    games_list = ['Игра первая',
                  'Игра вторая',
                  'Игра третья']
    games_num = ['game' + str(x) for x in range(1, 4)]
    context = dict(zip(games_num, games_list))
    return render(request, 'shop.html', context)


def basket(request):
    return render(request, 'basket.html')

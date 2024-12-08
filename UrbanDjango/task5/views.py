from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
users = ["user1",
         "user2",
         "user3"]
info = {}


def sign_up_by_django(request):
    # print(request.method)
    info["info_text"] = ""
    if request.method == "POST":
        form = UserRegister(request.POST)
        # print("форма заполнена - ", form.is_valid())
        # print("Поля доступа - ", form.cleaned_data)
        if form.is_valid():
            username = form.cleaned_data["username"]
            print("username :", username)
            password = form.cleaned_data["password"]
            print("password :", password)
            repeat_password = form.cleaned_data["repeat_password"]
            print("repeat_password :", repeat_password)
            age = form.cleaned_data["age"]
            print("age :", age)
            # return HttpResponse(parsing(username, password, repeat_password, age))
            info["info_text"] = parsing(username, password, repeat_password, age)
    form = UserRegister()
    info["form"] = form
    return render(request, 'reg_page.html', info)


def sign_up_by_html(request):
    # print(request.method)
    info["info_text"] = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        print("username:", username)
        print("password:", password)
        print("repeat_password:", repeat_password)
        print("age:", age)
        # return HttpResponse(parsing(username, password, repeat_password, age))
        info["info_text"] = parsing(username, password, repeat_password, age)
    return render(request, 'registration_page.html', info)


def parsing(username, password, repeat_password, str_age):
    info_text = "Извините, что то пошло не так."
    try:
        age = int(str_age)
        if username in users:
            info_text = "Пользователь уже существует"
        elif age < 18:
            info_text = "Вы должны быть старше 18"
        elif len(password) < 8:
            info_text = "Пароль должен быть не менее 8 символов."
        elif password == repeat_password:
            info_text = f"Приветствуем, {username}!"
        else:
            info_text = "Пароль не совпадает с повтором."
    except:
        info_text = "Возраст должен быть целым числом"
    print(info_text)
    return info_text

from django.http import HttpResponse


def data(request):
    return HttpResponse("<h1>Это страница для разной информации</h1>")


def test(request):
    return HttpResponse("<h1>Это страница для разных тестов</h1>")

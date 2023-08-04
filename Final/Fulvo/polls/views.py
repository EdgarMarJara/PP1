from django.http import HttpResponse


def index(request):
    return HttpResponse("Bienvenidos al sistema de reserva de canchas deportivas Fulvo")
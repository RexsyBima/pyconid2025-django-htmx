from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_pycon(request: HttpRequest):
    return render(
        request,
        "core/hello_pycon.html",
    )


def get_hello_pycon_answer(request: HttpRequest):
    return HttpResponse("Hello Pycon ID 2025")

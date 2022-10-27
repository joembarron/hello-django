"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import math
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path


def rectangleArea(request):
    try:
        width = int(request.GET.get('width'))
        height = int(request.GET.get('height'))
        response = HttpResponse("<h1>{}</h1>".format(width * height))
        response.status_code = 200
    except (TypeError):
        response = HttpResponse()
        response.status_code = 400

    return response


def rectangleAreaWithParams(request, height=1, width=1):
    response = HttpResponse("<h1>{}</h1>".format(height * width))
    return response


def rectanglePerimeter(request):
    try:
        width = int(request.GET.get('width'))
        height = int(request.GET.get('height'))
        response = HttpResponse("<h1>{}</h1>".format((2 * width + 2 * height)))
    except (TypeError):
        response = HttpResponse()
        response.status_code = 400

    return response


def rectanglePerimeterWithParams(request, height=1, width=1):
    response = HttpResponse("<h1>{}</h1>".format(2 * height + 2 * width))
    return response


def circleArea(request):
    try:
        radius = int(request.GET.get('radius'))
        response = HttpResponse("<h1>{}</h1>".format(math.pi * (radius ** 2)))
    except (TypeError):
        response = HttpResponse()
        response.status_code = 400

    return response


def circleAreaWithParams(request, radius):
    response = HttpResponse("<h1>{}</h1>".format(math.pi * (radius ** 2)))
    return response


def circlePerimeter(request):
    radius = int(request.GET.get('radius'))
    response = HttpResponse("<h1>{}</h1>".format(2 * math.pi * radius))
    return response


def circlePerimeterWithParams(request, radius):
    response = HttpResponse("<h1>{}</h1>".format(2 * math.pi * radius))
    return response


urlpatterns = [
    path("admin/", admin.site.urls),
    path("rectangle/area", rectangleArea),
    path("rectangle/perimeter", rectanglePerimeter),
    path("circle/area", circleArea),
    path("circle/perimeter", circlePerimeter),
    path("rectangle/area/<int:height>/<int:width>", rectangleAreaWithParams),
    path("rectangle/perimeter/<int:height>/<int:width>",rectanglePerimeterWithParams),
    path("circle/area/<int:radius>", circleAreaWithParams),
    path("circle/perimeter/<int:radius>", circlePerimeterWithParams),
]

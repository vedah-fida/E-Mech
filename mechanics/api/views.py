from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse


def test_view(request):
    view_name = "<h2>I am a view</h2>"
    return HttpResponse(view_name)

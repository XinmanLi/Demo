from django.shortcuts import render
import os


def linkchecker(request):
    context = {
        'page_title': 'LinkChecker'
    }
    return render(request, 'linkchecker/index.html', context)


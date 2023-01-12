from django.shortcuts import render


def home(request):
    """ホームページ"""
    return render(request, 'home.html')

from django.shortcuts import render

def home_page_view(request):
    return render(request, 'website/home.html')
def games_page_view(request):
    return render(request, 'website/games.html')
def posts_page_view(request):
    return render(request, 'website/home.html')
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/partials/pages/home.html', context={
        'name': 'Ubirajara'
    })





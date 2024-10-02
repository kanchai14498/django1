from django.shortcuts import render


def renderTemplate(request):
    return render(request, 'templatesApp/firstTemplate.html')

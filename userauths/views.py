from django.shortcuts import render


def RegisterView(request):
    return render(request, 'userauths/register.html')

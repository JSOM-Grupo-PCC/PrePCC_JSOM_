from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='contact:login')
def index(request):

    context = {
        'site_title': 'Contatos',
    }

    return render(
        request,
        'contact/index.html',
        context
    )

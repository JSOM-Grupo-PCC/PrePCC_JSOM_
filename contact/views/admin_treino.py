from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from contact.models import UserProfile

@user_passes_test(lambda u: u.is_staff)
def lista_usuarios(request):
    site_title = "Lista de Usuarios"
    users = UserProfile.objects.select_related('user').prefetch_related('user__treino_set')

    context = {
        'users': users,
        'site_title': site_title,
    }

    return render(request, 'contact/lista_usuarios.html', context)

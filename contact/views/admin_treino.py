from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from contact.models import UserProfile
from django.utils import timezone

@user_passes_test(lambda u: u.is_staff)
def lista_alunos(request):
    site_title = "Lista de Alunos"
    users = UserProfile.objects.select_related('user').prefetch_related('user__treino_set')

    context = {
        'users': users,
        'site_title': site_title,
    }

    return render(request, 'contact/lista_alunos.html', context)

# Adicione a nova view para o perfil do usuário
@user_passes_test(lambda u: u.is_staff)
def perfil_aluno(request, user_id):
    user_profile = get_object_or_404(UserProfile, user__id=user_id)
    site_title = f"Perfil do aluno {user_profile.user.username}"

    # Calcular idade a partir da data de nascimento
    if user_profile.data_nascimento:
        hoje = timezone.now().date()
        idade = hoje.year - user_profile.data_nascimento.year - ((hoje.month, hoje.day) < (user_profile.data_nascimento.month, user_profile.data_nascimento.day))
    else:
        idade = None

    context = {
        'user_profile': user_profile,
        'idade': idade,
        'site_title': site_title,
    }

    return render(request, 'contact/perfil_aluno.html', context)
from django.shortcuts import render, redirect
from .services import evento_services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.http.response import JsonResponse

# Create your views here.

"""def index(request):
    return redirect('listar_eventos')
"""
@login_required(login_url='/login')
def listar_eventos(request):
    eventos = evento_services.get_eventos(request.user)
    context = {
        'eventos': eventos,
    }
    return render(request, 'agenda.html', context)

def logout_user(request):
    logout(request)
    return redirect('/')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Credenciais Inválidas')
            return redirect('login_user')
    return render(request, 'login.html')

@login_required(login_url='/login')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = evento_services.get_evento_by_id(id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento_services.update_evento(id=id_evento,
                                          titulo=titulo,
                                          data_evento=data_evento,
                                          descricao=descricao,
                                          usuario=usuario)
        else:
            evento_services.cadastrar_evento(titulo=titulo, data_evento=data_evento, descricao=descricao, usuario=usuario)

    return redirect('/')

@login_required(login_url='/login')
def delete_evento(request, id):
    evento_services.delete_evento(id)
    return redirect('/')

def cadastrar_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha1 = request.POST.get('password1')
        senha2 = request.POST.get('password2')
        if senha1 != senha2:
            messages.error(request, 'Senhas não conferem')
        else:
            try:
                user = User.objects.get(username=usuario)
                messages.error(request, 'Usuário já existe')
            except:
                user = User.objects.create_user(username=usuario, password=senha1)
                user.save()
                auth_user = authenticate(username=usuario, password=senha1)
                if auth_user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, 'Erro no login')
    return render(request, 'usuario.html')

@login_required(login_url='/login')
def vencidos(request):
    eventos = evento_services.get_last_eventos(request.user)
    context = {
        'eventos': eventos,
    }
    return render(request, 'vencidos.html', context)


@login_required(login_url='/login')
def json_lista_evento(request):
    user = request.user
    eventos = evento_services.get_eventos(user).values()
    return JsonResponse(list(eventos), safe=False)


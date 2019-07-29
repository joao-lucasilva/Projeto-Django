from django.shortcuts import render,redirect
from website.models import Pessoa,Ideia

# Create your views here.
def index(request):
    if request.method == 'POST':
        email_form = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_form).first()
        print('Ta quase', pessoa)

        if pessoa is None:
            contexto = {'msg': 'Cadastre-se para criar uma ideia'}
            return render(request, 'cadastro.html', contexto)
        else:
            contexto = {'pessoa': pessoa}
            return render(request, 'ideias.html', contexto)

    return render(request, 'index.html', {})

def cadastro(request):
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        contexto = {"msg": 'Parabéns, faça login para começar a ter e ver ideias'}
        return render(request, 'index.html', contexto)

    return render(request, 'cadastro.html', contexto)

def sobre(request):
    ideias = Ideia.objects.all()
    args = {
        'ideias':ideias
    }
    return render(request, 'sobre.html', args)

def cadastrar_ideia(request):
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_pessoa).first()
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categoria = request.POST.get('categoria')
            ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save()
            print('ideia salva')

            return redirect('/sobre')

        return render(request, 'ideias.html', {})
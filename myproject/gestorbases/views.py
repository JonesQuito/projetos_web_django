from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, View
from myproject.gestorbases.forms import InsereBaseForm # importa o formulário
from myproject.gestorbases.forms import InsereTabelaForm
from myproject.gestorbases.forms import InsereAtualizacaoForm
from django.shortcuts import render
from django.http import HttpResponse
from myproject.gestorbases.models import Base, Tabela, Atualizacao

from myproject.models import Alunos

from django.contrib.auth.mixins import LoginRequiredMixin

# ---------- DEPENDÊNCIAS NECESSÁRIAS PARA IMPLEMENTAR A PAGINAÇÃO ----------
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator

from django.shortcuts import render
# ---------- DEPENDÊNCIAS NECESSÁRIAS PARA IMPLEMENTAR A PAGINAÇÃO ----------




# ########################### SISTEMA DE LOGIN ##########################

from django.contrib.auth import authenticate, logout, login as authlogin
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required


def login(request):
	if request.user.id:
		return render(request, 'gestorbases/logado.html',{})

	if request.POST:
		usuario = request.POST.get('usuario')
		senha = request.POST.get('senha')
		u = authenticate(request, username=usuario, password=senha)

		if(u is not None):
			if(u.is_active):
				authlogin(request, u)
				return redirect('gestorbases:dashboard')
				#return render(request, 'gestorbases/dashboard.html',{'user': u})
	return render(request, 'gestorbases/login.html', {})


def sair(request):
	logout(request)
	return render(request, 'gestorbases/login.html', {})


# ########################### SISTEMA DE LOGIN ##########################

# Create your views here.

def home(request):
	#return HttpResponse('Index do Gestor de bases')
	alunos = Alunos.alunos.all()
	contexto = {'alunos': alunos}
	return render(request, 'bases/index.html', contexto)

def logado(request):
	return render(request, 'gestorbases/logado.html',{})

@login_required
def dashboard(request):
	bases = Base.objetos.all()
	tabelas = Tabela.objetos.all()
	atualizacoes = Atualizacao.objetos.all()
	contexto = {'tabelas': tabelas, 'bases': bases, 'atualizacoes': atualizacoes}
	return render(request, 'gestorbases/dashboard.html', contexto)


'''
def cadastroBase(request):
	return render(request, 'gestorbases/cadastroBase.html', {})
'''

# CADASTRAMENTO DE BASE
# ----------------------------------------------

class BaseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'gestorbases/base/cadastroBase.html'
    model = Base
    form_class = InsereBaseForm
    success_url = reverse_lazy("gestorbases:lista_bases")


# LISTAGEM DE BASES
# ----------------------------------------------
'''
class BaseListView(LoginRequiredMixin, ListView):
	template_name = 'gestorbases/base/listaBases.html'
	model = Base
	context_object_name = 'bases'
'''
def listingBases(request):
	bases_lista = Base.objetos.all().order_by('nome')
	paginator = Paginator(bases_lista, 3)
	page = request.GET.get('page')
	bases = paginator.get_page(page)
	return render(request, 'gestorbases/base/listaBases.html', {'bases':bases})

# ATUALIZAÇÃO DE BASE
# ----------------------------------------------
class BaseUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'gestorbases/base/editaBase.html'
	model = Base
	fields = '__all__'
	context_object_name = 'base'
	success_url = reverse_lazy("gestorbases:lista_bases")


# EXCLUSÃO DE BASE
# ----------------------------------------------
class BaseDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'gestorbases/base/excluiBase.html'
	model = Base
	fields = '__all__'
	context_object_name = 'base'
	success_url = reverse_lazy('gestorbases:lista_bases')




# CADASTRAMENTO DE TABELA
# ----------------------------------------------
class TabelaCreateView(LoginRequiredMixin, CreateView):
	template_name = 'gestorbases/tabela/cadastroTabela.html'
	model = Tabela
	form_class = InsereTabelaForm
	success_url = reverse_lazy('gestorbases:lista_tabelas')


# LISTAGEM DE TABELAS
# ----------------------------------------------
'''
class TabelaListView(LoginRequiredMixin, ListView):
	template_name = 'gestorbases/tabela/listaTabelas.html'
	model = Tabela
	context_object_name = 'tabelas'
'''
def listingTables(request):
		tabelas_lista = Tabela.objetos.all().order_by('nome')
		paginator = Paginator(tabelas_lista, 7)
		page = request.GET.get('page')
		tabelas = paginator.get_page(page)
		return render(request, 'gestorbases/tabela/listaTabelas.html', {'tabelas': tabelas})

'''
def is_active_class(request):
	atual = request.GET.get('atual')
	pagina = request.GET.get('pagina')
	retorno = ''
	if pagina == atual:
		retorno = 'active'
	return retorno
'''
# EDIÇÃO DE TABELAS
# ----------------------------------------------
class TabelaUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'gestorbases/tabela/editaTabela.html'
	models = Tabela
	fields = '__all__'
	context_object_name = 'tabela'
	success_url = reverse_lazy('gestorbases:lista_tabelas')


	def get_object(self, queryset=None):
		tabela = None
		id = self.kwargs.get(self.pk_url_kwarg)
		if id is not None:
			# Busca o tabela apartir do id
			tabela = Tabela.objetos.filter(id=id).first()

		# Retorna o objeto encontrado
		return tabela
		

# EXCLUSÃO DE TABELA
# ----------------------------------------------
class TabelaDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'gestorbases/tabela/excluiTabela.html'
	model = Tabela
	fields = '__all__'
	context_object_name = 'tabela'
	success_url = reverse_lazy('gestorbases:lista_tabelas')



# REGISTRO DE NOVA ATUALIZAÇÃO
# ----------------------------------------------
class AtualizacaoCreateView(LoginRequiredMixin, CreateView):
	template_name = 'gestorbases/atualizacao/cadastroAtualizacao.html'
	model = Atualizacao
	form_class = InsereAtualizacaoForm
	success_url = reverse_lazy('gestorbases:nova_atualizacao')


# LISTAGEM DE ATUALIZAÇÕES
# ----------------------------------------------
class AtualizacaoListView(LoginRequiredMixin, ListView):	
	template_name = 'gestorbases/atualizacao/listaAtualizacoes.html'
	model = Atualizacao
	context_object_name = 'atualizacoes'



def listingAtualizacoes(request):
	atualizacoes_lista = Atualizacao.objetos.all().order_by('pk')
	paginator = Paginator(atualizacoes_lista, 5)
	page = request.GET.get('page')
	atualizacoes = paginator.get_page(page)
	return render(request, 'gestorbases/atualizacao/listaAtualizacoes.html', {'atualizacoes': atualizacoes})


# DETALHAMENTO DE ATUALIZAÇÃO
# ----------------------------------------------
class AtualizacaoDetalhesView(LoginRequiredMixin, UpdateView):
	template_name = 'gestorbases/atualizacao/detalhesAtualizacao.html'
	model = Atualizacao
	fields = '__all__'
	context_object_name = 'atualizacao'

	def get_object(self, queryset=None):
		atualizacao = None
		id = self.kwargs.get(self.pk_url_kwarg)
		if id is not None:
			atualizacao = Atualizacao.objetos.filter(id=id).first()
		return atualizacao



class AtualizacaoUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'gestorbases/atualizacao/editaAtualizacao.html'
	model = Atualizacao
	fields = '__all__'
	context_object_name = 'atualizacao'
	success_url = reverse_lazy('gestorbases:lista_atualizacoes')

	def get_object(self, queryset=None):
		atualizacao = None
		id = self.kwargs.get(self.pk_url_kwarg)
		if id is not None:
			atualizacao = Atualizacao.objetos.filter(id=id).first()
		return atualizacao


# EXCLUSÃO DE ATUALIZAÇÃO
# ----------------------------------------------
class AtualizacaoDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'gestorbases/atualizacao/excluiAtualizacao.html'
	model = Atualizacao
	fields = '__all__'
	context_object_name = 'atualizacao'
	success_url = reverse_lazy('gestorbases:lista_atualizacoes')





def teste(request):
	tabelas = Tabela.objetos.all()
	if request.POST:
		tabela = request.POST.get('tabela')
		tabelas = Tabela.objetos.filter(nome__icontains=tabela)
		return render(request,'gestorbases/teste.html', {'tabelas':tabelas})
	return render(request,'gestorbases/teste.html', {'tabelas':tabelas})





'''

class AtualizacaoDetalhesView(LoginRequiredMixin, UpdateView):
	template_name = 'gestorbases/atualizacao/detalhesAtualizacao.html'
	model = Atualizacao
	fields = '__all__'
	context_object_name = 'atualizacao'

	def get_object(self, queryset=None):
		atualizacao = None
		id = self.kwargs.get(self.pk_url_kwarg)
		if id is not None:
			atualizacao = Atualizacao.objetos.filter(id=id).first()
		return atualizacao

		usuario = request.POST.get('usuario')
		senha = request.POST.get('senha')
'''





















class AlunosListView(ListView):
	template_name = 'bases/index.html'
	model = Alunos
	context_object_name = 'alunos'




class AlunosUpdateView(UpdateView):
	template_name = 'bases/editaAluno.html'
	model = Alunos
	fields = ['seq_geral', 'matricula', 'nome', 'nome_mae'] # Lista de campos disponibilizados para edição
	context_object_name = 'aluno'

	def get_object(self, queryset=None):
		aluno = None
		id = self.kwargs.get(self.pk_url_kwarg)
		slug = self.kwargs.get(self.slug_url_kwarg)
		if id is not None:
			# Busca o aluno apartir do id
			aluno = Alunos.alunos.filter(seq_geral=id).first()
		elif slug is not None:
			# Pega o campo slug do Model
			campo_slug = self.get_slug_field()
			# Busca o aluno apartir do slug
			aluno = Alunos.alunos.filter(**{campo_slug: slug}).first()
		# Retorna o objeto encontrado
		return aluno


# EXEMPLOS DE VIEWS BASEADAS EM FUNÇÕES (BVF)
'''
def listaBases(request):
	return render(request, 'gestorbases/listaBases.html', {})

'''
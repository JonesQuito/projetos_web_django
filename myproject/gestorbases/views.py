from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from myproject.gestorbases.forms import InsereBaseForm # importa o formulário
from myproject.gestorbases.forms import InsereTabelaForm
from myproject.gestorbases.forms import InsereAtualizacaoForm
from django.shortcuts import render
from django.http import HttpResponse
from myproject.gestorbases.models import Base, Tabela, Atualizacao

from myproject.models import Alunos

# Create your views here.

def home(request):
	#return HttpResponse('Index do Gestor de bases')
	alunos = Alunos.alunos.all()
	contexto = {'alunos': alunos}
	return render(request, 'bases/index.html', contexto)


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

class BaseCreateView(CreateView):
    template_name = 'gestorbases/base/cadastroBase.html'
    model = Base
    form_class = InsereBaseForm
    success_url = reverse_lazy("gestorbases:lista_bases")


# LISTAGEM DE BASES
# ----------------------------------------------
class BaseListView(ListView):
	template_name = 'gestorbases/base/listaBases.html'
	model = Base
	context_object_name = 'bases'


# ATUALIZAÇÃO DE BASE
# ----------------------------------------------
class BaseUpdateView(UpdateView):
	template_name = 'gestorbases/base/editaBase.html'
	model = Base
	fields = '__all__'
	context_object_name = 'base'
	success_url = reverse_lazy("gestorbases:lista_bases")


# EXCLUSÃO DE BASE
# ----------------------------------------------
class BaseDeleteView(DeleteView):
	template_name = 'gestorbases/base/excluiBase.html'
	model = Base
	fields = '__all__'
	context_object_name = 'base'
	success_url = reverse_lazy('gestorbases:lista_bases')


# CADASTRAMENTO DE TABELA
# ----------------------------------------------
class TabelaCreateView(CreateView):
	template_name = 'gestorbases/tabela/cadastroTabela.html'
	model = Tabela
	form_class = InsereTabelaForm


# LISTAGEM DE TABELAS
# ----------------------------------------------
class TabelaListView(ListView):	
	template_name = 'gestorbases/tabela/listaTabelas.html'
	model = Tabela
	context_object_name = 'tabelas'



# EDIÇÃO DE TABELAS
# ----------------------------------------------
class TabelaUpdateView(UpdateView):
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
class TabelaDeleteView(DeleteView):
	template_name = 'gestorbases/tabela/excluiTabela.html'
	model = Tabela
	fields = '__all__'
	context_object_name = 'tabela'
	success_url = reverse_lazy('gestorbases:lista_tabelas')



# REGISTRO DE NOVA ATUALIZAÇÃO
# ----------------------------------------------
class AtualizacaoCreateView(CreateView):
	template_name = 'gestorbases/atualizacao/cadastroAtualizacao.html'
	model = Atualizacao
	form_class = InsereAtualizacaoForm
	success_url = reverse_lazy('gestorbases:nova_atualizacao')


# LISTAGEM DE ATUALIZAÇÕES
# ----------------------------------------------
class AtualizacaoListView(ListView):	
	template_name = 'gestorbases/atualizacao/listaAtualizacoes.html'
	model = Atualizacao
	context_object_name = 'atualizacoes'


# DETALHAMENTO DE ATUALIZAÇÃO
# ----------------------------------------------
class AtualizacaoDetalhesView(UpdateView):
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



class AtualizacaoUpdateView(UpdateView):
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
class AtualizacaoDeleteView(DeleteView):
	template_name = 'gestorbases/atualizacao/excluiAtualizacao.html'
	model = Atualizacao
	fields = '__all__'
	context_object_name = 'atualizacao'
	success_url = reverse_lazy('gestorbases:lista_atualizacoes')























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
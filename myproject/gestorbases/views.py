from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from myproject.gestorbases.models import Base
from myproject.gestorbases.forms import InsereBaseForm # importa o formulário
from django.shortcuts import render
from django.http import HttpResponse

from myproject.models import Alunos

# Create your views here.

def home(request):
	#return HttpResponse('Index do Gestor de bases')
	alunos = Alunos.alunos.all()
	contexto = {'alunos': alunos}
	return render(request, 'bases/index.html', contexto)


def dashboard(request):
	return render(request, 'gestorbases/dashboard.html', {})


'''
def cadastroBase(request):
	return render(request, 'gestorbases/cadastroBase.html', {})
'''

# CADASTRAMENTO DE BASE
# ----------------------------------------------

class BaseCreateView(CreateView):
    template_name = 'gestorbases/cadastroBase.html'
    model = Base
    form_class = InsereBaseForm
    success_url = reverse_lazy("gestorbases:lista_bases")


# LISTAGEM DE BASES
# ----------------------------------------------
class BaseListView(ListView):
	template_name = 'gestorbases/listaBases.html'
	model = Base
	context_object_name = 'bases'


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------
class BaseUpdateView(UpdateView):
	template_name = 'gestorbases/editaBase.html'
	model = Base
	fields = '__all__'
	context_object_name = 'base'
	success_url = reverse_lazy("gestorbases:lista_bases")


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
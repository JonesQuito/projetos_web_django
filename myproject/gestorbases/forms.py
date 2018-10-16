from django import forms
from myproject.gestorbases.models import Base, Tabela, Atualizacao


# FORMULÁRIO DE INCLUSÃO DE BASES
# -------------------------------------------
class InsereBaseForm(forms.ModelForm):
	
	class Meta:
		# Modelo 
		model = Base
		# Campos que estarão no form
		fields = ['nome', 'descricao', 'atualizacao', 'host', 'owner']


class InsereTabelaForm(forms.ModelForm):
    class Meta:
        # Modelo
        model = Tabela
        # Campos que estarão no form
        fields = ['base', 'nome', 'descricao', 'esquema']


class InsereAtualizacaoForm(forms.ModelForm):
    class Meta:
        # Modelo
        model = Atualizacao
        # Campos que estarão no fomr
        fields = ['tabela', 'responsavel', 'observacoes', 'mes_ref', 'ano_ref', 'origem_dados']


    def filteringTables(request):
        tabela = request.GET.get('tabela')
        tabelas = Tabela.objetos.filter(nome__icontains=tabela)
        return tabelas

        
        




# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------
'''
class InsereFuncionarioForm(forms.ModelForm):

    chefe = forms.BooleanField(
        label='Chefe?',
        required=False,
    )

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Funcionario

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'tempo_de_servico',
            'remuneracao'
        ]
'''
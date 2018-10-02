from django import forms
from myproject.gestorbases.models import Base


# FORMULÁRIO DE INCLUSÃO DE BASES
# -------------------------------------------
class InsereBaseForm(forms.ModelForm):
	
	class Meta:
		# Modelo 
		model = Base

		# Campos que estarão no form
		fields = ['nome', 'descricao', 'atualizacao', 'host', 'owner']





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
from django.contrib import admin
from django.urls import path
from myproject.gestorbases import views

app_name='gestorbases'

urlpatterns = [
	path('', views.home, name='home'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('bases/nova', views.BaseCreateView.as_view(), name='nova_base'),
	path('bases/lista', views.BaseListView.as_view(), name='lista_bases'),
	path('bases/atualiza/<pk>', views.BaseUpdateView.as_view(), name='atualiza_base'),


	path('alunos/', views.AlunosListView. as_view(), name='lista_alunos'),
	#path('atualizar/aluno/<pk>', views.AlunosUpdateView.as_view()),
    path('admin/', admin.site.urls),
]
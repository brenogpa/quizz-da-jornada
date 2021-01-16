from django.contrib import admin

# Register your models here.
from quiz_devpro.quiz.models import Pergunta, Aluno, Respostas


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['id', 'enunciado', 'disponivel']


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'criacao']


@admin.register(Respostas)
class RespostasAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'pergunta', 'pontos', 'criacao']

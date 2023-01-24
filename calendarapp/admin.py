from django.contrib import admin
from calendarapp import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = [
        "id",
        "title",
        "user",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]


@admin.register(models.EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = models.EventMember
    list_display = ["id", "event", "user", "created_at", "updated_at"]
    list_filter = ["event"]

@admin.register(models.Pessoa)
class PessoasAdmin(admin.ModelAdmin):
    model = models.Pessoa
    list_display = ['nome', 'sobrenome', 'cpf', 'data_nascimento', 'numero_de_telefone' ]
    list_filter = ["nome"]

@admin.register(models.Clientes)
class ClientAdmin(admin.ModelAdmin):
    model = models.Clientes
    list_display = [

        'rua',
        'logradouro',
        'setor',
        'pessoa',
     ]
    # list_filter = ["nome"]
@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    model = models.Funcionario
    list_display = [
        'funcao',
        'pessoa_id',
        'pessoa_id1'
    ]
    # list_filter = ["nome"]
@admin.register(models.Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    model = models.Atendimento
    list_display = [
        'horario',
        'detalhes',
        'criado_em',
        'atualizado_em',
        'reagendado',
        'funcionario',
        'clientes']
    search_fields = ["detalhes"]
    list_filter = ["atualizado_em"]

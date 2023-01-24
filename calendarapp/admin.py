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
    list_display = [
        'nome',
        'cpf',
        'sexo',
        'data_nascimento',
        'estado_civel',
        'numero_de_telefone',
        'telefone_e_whatsapp',
        ]
    list_filter = ["nome"]
    search_fields = ["nome" , "cpf"]

@admin.register(models.Clientes)
class ClientAdmin(admin.ModelAdmin):
    model = models.Clientes
    list_display = [
        'pessoa',
        'cep',
        'logradouro',
        'numero',
        'complemento',
        'estado',
        'municipio',
        'bairro',
        'divisao_interna',
        'tipo_de_imovel',
        
    ]
    list_filter = ["pessoa"]
    search_fields = ["cep" , "pessoa"]
@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    model = models.Funcionario
    list_display = [
        'pessoa',
        'funcao',
        
    ]
    search_fields = ["pessoa"]

@admin.register(models.Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    model = models.Atendimento
    list_display = [
        'clientes',
        'helpdesk',
        'detalhes',
        'horario',
        'funcionario',
        'empresa',
        'reagendado',
        'criado_em',
        'atualizado_em',
        
        ]
    search_fields = ["detalhes"]
    list_filter = ["atualizado_em"]

@admin.register(models.Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    model = models.Empresa
    list_display = [
        'nome',
    ]
    list_filter = ["nome"]
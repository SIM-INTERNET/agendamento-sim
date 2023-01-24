# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Pessoa(models.Model):
    sexo_escolha = (
    ('MASCULINO','masculino'),
    ('FEMININO','feminino'))
    estado_civel_escolha = (
    ('CASADO','casado'),
    ('SOLTEIRO','solteiro'))
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(choices=sexo_escolha,max_length=14)
    data_nascimento = models.DateField()
    estado_civel = models.CharField(choices=estado_civel_escolha,max_length=14)
    numero_de_telefone = models.CharField(max_length=17)
    telefone_e_whatsapp = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    

    class Meta:
        managed = False
        db_table = 'pessoa'

class Funcionario(models.Model):
    funcao_escolha = (
    ('TECNICO','tecnico'),
    ('ADM','adm'))
    funcao = models.CharField(choices=funcao_escolha,max_length=14)
    pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='Pessoa_id')  # Field name made lowercase.

    def __str__(self):
        retorno = f'{self.funcao} | {self.pessoa}'
        return str( retorno)
    

    class Meta:
        managed = False
        db_table = 'funcionario'

class Clientes(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    divisao_interna = models.CharField(max_length=50, blank=True, null=True)
    tipo_de_imovel = models.CharField(max_length=50)
    pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='Pessoa_id')  # Field name made lowercase.
    def __str__(self):
        return str(self.pessoa)  
    
    class Meta:
        managed = False
        db_table = 'clientes'

class Atendimento(models.Model):
    helpdesk = models.CharField(max_length=60)
    horario = models.DateTimeField(db_column='Horario')  # Field name made lowercase.
    detalhes = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    reagendado = models.BooleanField(default=False)
    clientes = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='Clientes_id')  # Field name made lowercase.
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='Funcionario_id')  # Field name made lowercase.

    def __str__(self):
        return str(self.clientes)

    class Meta:
        managed = False
        db_table = 'atendimento'
        unique_together = (('id', 'empresa'),)

class Empresa(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    nome = models.CharField(max_length=45)
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'empresa'
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    numero_de_telefone = models.CharField(max_length=17)

    # def __str__(self):
    #     return self.nome

    class Meta:
        managed = False
        db_table = 'pessoa'

class Funcionario(models.Model):
    funcao = models.CharField(max_length=50)
    pessoa_id = models.IntegerField(db_column='Pessoa_id')  # Field name made lowercase.
    pessoa_id1 = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='Pessoa_id1')  # Field name made lowercase.

    # def __str__(self):
    #     return f'{self.funcao} po',
    
    class Meta:
        managed = False
        db_table = 'funcionario'
        unique_together = (('id', 'pessoa_id1'),)

class Clientes(models.Model):
    rua = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=50)
    setor = models.CharField(max_length=50)
    pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='Pessoa_id')  # Field name made lowercase.

    def __str__(self):
        return self.logradouro

    class Meta:
        managed = False
        db_table = 'clientes'
        unique_together = (('id', 'pessoa'),)

class Atendimento(models.Model):
    horario = models.DateTimeField(db_column='Horario')  # Field name made lowercase.   
    detalhes = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    reagendado = models.BooleanField(default=False)
    funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='Funcionario_id')  # Field name made lowercase.
    clientes = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='Clientes_id')  # Field name made lowercase.

    def __str__(self):
        return self.detalhes

    class Meta:
        managed = False
        db_table = 'atendimento'
        unique_together = (('id', 'funcionario', 'clientes'),)
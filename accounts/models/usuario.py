from django.db import models

class  Pessoa(models.Model):
    nome = models.CharField(max_length=20), 
    sobrenome = models.CharField(max_length=30),
    cpf = models.CharField(max_length=14),   #066.368.171.51
    data_nascimento = models.DateField(), 
    numero_de_telefone = models.CharField(max_length=17),  #(63) 9 99234-8828
    def __str__(self):
        return self.nome + ' ' + self.sobrenome
    

class  Clientes(models.Model):
    '''Avenida Ipanema Quadra 39 lote'''
    rua = models.CharField(max_length=50),
    logradouro = models.CharField(max_length=50),
    setor = models.CharField(max_length=50),
    def __str__(self):
        return self.rua  + ' ' + self.logradouro

class  Atendimento(models.Model):

    escolhas_status = (
        (INICIADO, "Iniciado"),
        (EM_ATENDIMENTO, "Em Atendimento"),
        (COMCLUIDO, "Comcluido"),
    )

    Horario = models.DateTimeField() 
    status = models.CharField(max_length=14,choices=escolhas_status,default=INICIADO),
    detalhes = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    reagendado = models.BooleanField(default=False)  
    def __str__(self):
        return self.status

class  Funcionario(models.Model):
    '''Avenida Ipanema Quadra 39 lote'''
    foto_perfil = models.ImageField(upload_to='static/images/PefilFuncionario/%Y/%m/%d')
    funcao = models.CharField(max_length=50),
    def __str__(self):
        return self.funcao

    
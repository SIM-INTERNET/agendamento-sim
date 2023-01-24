# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    email = models.CharField(unique=True, max_length=255)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accounts_user'


class AccountsUserGroups(models.Model):
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_groups'
        unique_together = (('user', 'group'),)


class AccountsUserUserPermissions(models.Model):
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_user_permissions'
        unique_together = (('user', 'permission'),)





class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CalendarappEvent(models.Model):
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    title = models.CharField(unique=True, max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendarapp_event'


class CalendarappEventmember(models.Model):
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    event = models.ForeignKey(CalendarappEvent, models.DO_NOTHING)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendarapp_eventmember'
        unique_together = (('event', 'user'),)





class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'




class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=9)
    data_nascimento = models.DateField()
    estado_sivel = models.CharField(max_length=9)
    numero_de_telefone = models.CharField(max_length=17)
    telefone_e_whatsapp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pessoa'

class Funcionario(models.Model):
    funcao = models.CharField(max_length=50)
    pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='Pessoa_id')  # Field name made lowercase.

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
    divisÒo_interna = models.CharField(max_length=50)
    tipo_de_imovel = models.CharField(max_length=50)
    pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='Pessoa_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'

class Atendimento(models.Model):
    helpdesk = models.CharField(max_length=60)
    horario = models.DateTimeField(db_column='Horario')  # Field name made lowercase.
    detalhes = models.TextField()
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()
    reagendado = models.IntegerField()
    clientes = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='Clientes_id')  # Field name made lowercase.
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='Funcionario_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atendimento'
        unique_together = (('id', 'empresa'),)

class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'empresa'
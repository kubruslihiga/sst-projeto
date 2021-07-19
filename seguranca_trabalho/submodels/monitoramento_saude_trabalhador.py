from seguranca_trabalho.submodels.funcionario import Funcionario
from django.db import models
from .enums import get_choices
from .empresa import Empresa

class TipoExame:
    ADMISSIONAL=0
    PERIODICO=1
    RETORNO_TRABALHO=2
    MUDANCA_FUNCAO=3
    MONITORACAO_PONTUAL=4
    DEMISSIONAL=9

class ResultadoASO:
    APTO=1
    INAPTO=2

class OrdemExame:
    REFERENCIAL=1
    SEQUENCIAL=2

class Procedimento(models.Model):
    __tablename__ = "sst_procedimento"
    class Meta:
        verbose_name="Procedimento"
        verbose_name_plural="Procedimentos"
    codigo = models.CharField(max_length=30, null=False, verbose_name="Código")
    nome = models.CharField(max_length=250, null=False, verbose_name="Nome")
    def __str__(self) -> str:
        return self.codigo + " - " + self.nome

class MedicoASO(models.Model):
    __tablename__ = "sst_medico_aso"
    class Meta:
        verbose_name="Médico ASO"
        verbose_name_plural="Médicos ASO"
    cpf = models.CharField(max_length=13, null=False, verbose_name="CPF")
    nit = models.CharField(max_length=30, null=False, verbose_name="NIT")
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome")
    numero_inscricao = models.CharField(max_length=20, null=False, verbose_name="Número de inscrição")
    uf = models.CharField(max_length=10, null=False, verbose_name="UF")

class MonitoramentoSaudeTrabalhador(models.Model):
    __tablename__ = "sst_monitoramento_saude"
    class Meta:
        verbose_name="Monitoramento de saúde do trabalhador"
        verbose_name_plural="Monitoramento de saúde do trabalhador"
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=False, verbose_name="Empresa")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, null=False, verbose_name="Funcionário")
    estagiario = models.BooleanField(null=False, default=False, verbose_name="Estagiário")
    tipo_exame = models.IntegerField(choices=get_choices(TipoExame), null=False, verbose_name="Tipo de exame")
    data_aso = models.DateTimeField(null=False, verbose_name="Data do ASO")
    resultado_aso = models.IntegerField(choices=get_choices(ResultadoASO), null=False, verbose_name="Resultado do ASO")
    medico_aso_cpf = models.CharField(max_length=13, null=True, verbose_name="CPF")
    medico_aso_nit = models.CharField(max_length=30, null=True, verbose_name="NIT")
    medico_aso_nome = models.CharField(max_length=150, null=True, verbose_name="Nome")
    medico_aso_numero_inscricao = models.CharField(max_length=20, null=True, verbose_name="Número de inscrição")
    medico_aso_uf = models.CharField(max_length=10, null=True, verbose_name="UF")
    # coordenador do PCMSO
    coordenador_cpf = models.CharField(max_length=13, null=False, verbose_name="CPF")
    coordenador_crm = models.CharField(max_length=20, null=False, verbose_name="Número CRM")
    coordenador_uf = models.CharField(max_length=20, null=False, verbose_name="UF")
    coordenador_nome = models.CharField(max_length=150, null=False, verbose_name="Nome")

class Exame(models.Model):
    data_exame = models.DateTimeField(null=False, verbose_name="Data do exame")
    procedimento = models.ForeignKey(Procedimento, null=False, on_delete=models.PROTECT, verbose_name="Procedimento")
    observacao_procedimento = models.CharField(max_length=1000, null=True, verbose_name="Observação do procedimento")
    ordem_exame = models.IntegerField(choices=get_choices(OrdemExame), null=False, verbose_name="Ordem do exame")
    monitoramento_saude_trabalhador = models.ForeignKey(MonitoramentoSaudeTrabalhador, on_delete=models.PROTECT, verbose_name="Monitoramento saúde do trabalhador")
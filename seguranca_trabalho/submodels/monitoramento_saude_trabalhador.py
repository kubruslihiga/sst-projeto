from django.db import models
from .enums import get_choices

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
    codigo = models.CharField(max_length=30, null=False)
    nome = models.CharField(max_length=250, null=False)

class MedicoASO(models.Model):
    __tablename__ = "sst_medico_aso"
    class Meta:
        verbose_name="Médico ASO"
        verbose_name_plural="Médicos ASO"
    cpf = models.CharField(max_length=13, null=False)
    nit = models.CharField(max_length=30, null=False)
    nome = models.CharField(max_length=150, null=False)
    numero_inscricao = models.CharField(max_length=20, null=False)
    uf = models.CharField(max_length=10, null=False)

class MonitoramentoSaudeTrabalhador(models.Model):
    __tablename__ = "sst_monitoramento_saude"
    class Meta:
        verbose_name="Monitoramento de saúde do trabalhador"
        verbose_name_plural="Monitoramento de saúde do trabalhador"
    # empresa = relationship("Empresa")
    # empresa_id = Column(Integer, ForeignKey('sst_empresa.id'), comment="Id da empresa", doc="Id da empresa")
    empresa_id = models.IntegerField(null=True)
    # funcionario = relationship("Funcionario")
    # funcionario_id = Column(Integer, ForeignKey('sst_funcionario.id'), comment="Id do funcionario", doc="Id do funcionario")
    funcionario_id = models.IntegerField(null=True)
    estagiario = models.BooleanField(null=False, default=False)
    tipo_exame = models.IntegerField(choices=get_choices(TipoExame), null=False)
    data_aso = models.DateTimeField(null=False)
    resultado_aso = models.IntegerField(choices=get_choices(ResultadoASO), null=False)
    data_exame = models.DateTimeField(null=False)
    procedimento = models.ForeignKey(Procedimento, null=False, on_delete=models.PROTECT)
    observacao_procedimento = models.CharField(max_length=1000, null=True)
    ordem_exame = models.IntegerField(choices=get_choices(OrdemExame), null=False)
    indicacao_resultado = models.IntegerField(null=False)
    medicos = models.ManyToManyField(MedicoASO)
    coordenador_cpf = models.CharField(max_length=13, null=False)
    coordenador_crm = models.CharField(max_length=20, null=False)
    coordenador_uf = models.CharField(max_length=20, null=False)
    coordenador_nome = models.CharField(max_length=150, null=False)

from django.db import models
from .enums import Genero, get_choices
from .empresa import Empresa

class LocalAmbiente:
    ESTABELECIMENTO_PROPRIO_EMPREGADOR=1
    ESTABELECIMENTO_TERCEIROS=2
    PRESTACAO_SERVICOS_INSTALACOES_TERCEIROS=3

class LotacaoTributaria(models.Model):
    __tablename__ = "sst_lotacao_tributaria"
    class Meta:
        verbose_name="Lotação tributária"
        verbose_name_plural="Lotações tributárias"
    codigo = models.CharField(max_length=15, null=True)
    descricao = models.CharField(max_length=750, null=True)

class AmbienteTrabalho(models.Model):
    __tablename__ = "sst_ambiente_trabalho"
    id = Column(Integer, Sequence('ambiente_trabalho_id_sequence'), primary_key=True)
    empresa = relationship("Empresa")
    empresa_id = Column(Integer, ForeignKey('sst_empresa.id'), comment="Id da empresa", doc="Id da empresa")
    cpf = models.CharField(max_length=13, null=False, comment="CPF")
    lotacoes_tributarias = relationship('LotacaoTributaria', secondary=sst_ambiente_trabalho_lotacoes)
    codigo = models.CharField(max_length=15, null=False)
    data_inicial = Column(Date, null=False, comment="Data")
    data_final = Column(Date, null=False, comment="Data final")
    nome = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=500, null=False, comment="Descricao ambiente trabalho")
    local_ambiente = Column(Enum(LocalAmbiente), null=False)
    tipo_inscricao = models.CharField(max_length=100, null=False)
    numero_inscricao = models.CharField(max_length=100, null=False)
    codigo_lotacao_tributaria = models.CharField(max_length=100, null=False)
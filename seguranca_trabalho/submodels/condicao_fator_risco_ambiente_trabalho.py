from django.db import models
from .enums import get_choices
from .funcionario import Funcionario
from .empresa import Empresa

class Atividade(models.Model):
    __tablename__ = "sst_atividade"
    # id = models.IntegerField(Sequence('atividade_id_sequence'), primary_key=True)
    class Meta:
        verbose_name="Atividade"
        verbose_name_plural="Atividades"
    codigo = models.CharField(max_length=20, null=False)
    descricao = models.CharField(max_length=2000, null=False)
    categoria = models.CharField(max_length=200, null=False)

class FatorRisco(models.Model):
    __tablename__ = "sst_fator_risco"
    class Meta:
        verbose_name="Fator de risco"
        verbose_name_plural="Fatores de risco"
    # id = models.IntegerField(Sequence('fator_risco_id_sequence'), primary_key=True)
    codigo = models.CharField(max_length=20, null=False)
    descricao = models.CharField(max_length=2000, null=False)
    categoria = models.CharField(max_length=200, null=False)

class UnidadeMedida(models.Model):
    __tablename__ = "sst_unidade_medida"
    class Meta:
        verbose_name="Unidade de medida"
        verbose_name_plural="Unidades de medida"
    # id = models.IntegerField(Sequence('unidade_medida_id_sequence'), primary_key=True)
    codigo = models.CharField(max_length=20, null=False)
    descricao = models.CharField(max_length=2000, null=False)

class OrgaoClasse:
    CRM = 1
    CREA = 2
    OUTROS = 9

class CriterioAvaliacao:
    QUANTITATIVO=1
    QUALITATIVO=2

class ToleranciaQualitativa:
    SILICA='SILICA'
    CALOR='CALOR'

class UtilizacaoEPC:
    NAO_SE_APLICA=0
    NAO_IMPLEMENTA=1
    IMPLEMENTA=2

class UtilizacaoEPI:
    NAO_SE_APLICA=0
    NAO_UTILIZA=1
    UTILIZA=2

class ResponsavelRegistroAmbiental(models.Model):
    class Meta:
        verbose_name="Responsável pelo registro ambiental"
        verbose_name_plural="Responsáveis pelo registro ambiental"
    __tablename__ = "sst_resp_registro_ambiental"
    cpf = models.CharField(max_length=13, null=False)
    nis = models.CharField(max_length=20, null=True)
    nome = models.CharField(max_length=150, null=False)
    orgao_classe = models.IntegerField(choices=get_choices(OrgaoClasse), null=False)
    sigla_orgao = models.CharField(max_length=20, null=True)
    numero_inscricao = models.CharField(max_length=30, null=False)
    uf = models.CharField(max_length=20, null=False)
    #condicao_fator_risco = models.ForeignKey(CondicaoFatorRisco, on_delete=models.PROTECT)

class AnaliseEPI(models.Model):
    __tablename__ = "sst_analise_epi"
    class Meta:
        verbose_name="Análise de EPI"
        verbose_name_plural="Análises de EPI"
    certificacao_epi = models.CharField(max_length=200, null=True)
    descricao_epi = models.CharField(max_length=1500, null=True)
    epi_eficaz = models.BooleanField(null=False, default=False)
    hierarquia_medida_protecao_coletiva = models.BooleanField(null=False, default=False)
    observada_condicao_funcionamento = models.BooleanField(null=False, default=False)
    observado_epi = models.BooleanField(null=False, default=False)
    observado_prazo_validade_ca = models.BooleanField(null=False, default=False)
    observado_periodicidade_troca = models.BooleanField(null=False, default=False)
    observada_higienizacao_epi = models.BooleanField(null=False, default=False)

class CondicaoFatorRisco(models.Model):
    class Meta:
        verbose_name="Condição de fator risco"
        verbose_name_plural="Condições de fator risco"
    __tablename__ = "sst_condicao_fator_risco"
    empresa = models.ForeignKey(Empresa, null=False, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, null=False, on_delete=models.PROTECT)
    data_inicio = models.DateTimeField(null=False)
    descricao_atividade_ambiente = models.CharField(max_length=1000, null=True)
    atividades = models.ManyToManyField(Atividade)
    fator_risco = models.ForeignKey(FatorRisco, on_delete=models.PROTECT)
    tipo_avaliacao = models.IntegerField(choices=get_choices(CriterioAvaliacao), null=False)
    intensidade = models.IntegerField(null=False)
    limite_tolerancia = models.IntegerField(null=True) #tem coisa errada
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT)
    tecnica_utilizada = models.CharField(max_length=1000, null=False)
    insalubridade = models.BooleanField(default=False, null=False)
    periculosidade = models.BooleanField(default=False, null=False)
    aposentadoria_especial = models.BooleanField(default=False, null=False)
    utilizacao_epc = models.IntegerField(choices=get_choices(UtilizacaoEPC), null=False)
    epc_eficaz = models.BooleanField(null=False, default=False)
    utilizacao_epi = models.IntegerField(choices=get_choices(UtilizacaoEPI), null=False)
    analises_epi = models.ForeignKey(AnaliseEPI, related_name="condicao_fator_risco", on_delete=models.PROTECT)
    responsaveis_registro_ambiental = models.ForeignKey(ResponsavelRegistroAmbiental, related_name="condicao_fator_risco", on_delete=models.PROTECT)
    metodologia_riscos_ergonomicos = models.CharField(max_length=1000, null=True)
    observacao = models.CharField(max_length=1000, null=False)

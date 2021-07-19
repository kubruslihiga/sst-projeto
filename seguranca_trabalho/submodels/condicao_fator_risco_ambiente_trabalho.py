from django.db import models
from django.db.models.deletion import PROTECT
from .enums import get_choices
from .funcionario import Funcionario
from .empresa import Empresa

class Atividade(models.Model):
    __tablename__ = "sst_atividade"
    class Meta:
        verbose_name="Atividade"
        verbose_name_plural="Atividades"
    codigo = models.CharField(max_length=20, null=False, verbose_name="Código")
    descricao = models.CharField(max_length=2000, null=False, verbose_name="Descrição")
    categoria = models.CharField(max_length=200, null=False, verbose_name="Categoria")
    def __str__(self) -> str:
        return self.codigo + " - " + self.descricao

class FatorRisco(models.Model):
    __tablename__ = "sst_fator_risco"
    class Meta:
        verbose_name="Fator de risco"
        verbose_name_plural="Fatores de risco"
    codigo = models.CharField(max_length=20, null=False, verbose_name="Código")
    descricao = models.CharField(max_length=2000, null=False, verbose_name="Descrição")
    categoria = models.CharField(max_length=200, null=False, verbose_name="Categoria")
    def __str__(self) -> str:
        return self.codigo + " - " + self.descricao

class UnidadeMedida(models.Model):
    __tablename__ = "sst_unidade_medida"
    class Meta:
        verbose_name="Unidade de medida"
        verbose_name_plural="Unidades de medida"
    codigo = models.CharField(max_length=20, null=False, verbose_name="Código")
    descricao = models.CharField(max_length=2000, null=False, verbose_name="Descrição")

    def __str__(self) -> str:
        return self.codigo + " - " + self.descricao

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
    cpf = models.CharField(max_length=13, null=False, verbose_name="CPF")
    nis = models.CharField(max_length=20, null=True, verbose_name="NIS")
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome")
    orgao_classe = models.IntegerField(choices=get_choices(OrgaoClasse), null=False, verbose_name="Órgão de classe")
    sigla_orgao = models.CharField(max_length=20, null=True, verbose_name="Sigla do órgão (outros)")
    numero_inscricao = models.CharField(max_length=30, null=False, verbose_name="Número de inscrição")
    uf = models.CharField(max_length=20, null=False, verbose_name="UF")
    #condicao_fator_risco = models.ForeignKey(CondicaoFatorRisco, on_delete=models.PROTECT)

class CondicaoAmbientalFatorRisco(models.Model):
    class Meta:
        verbose_name="Condição ambiental de fator risco"
        verbose_name_plural="Condições ambientais de fator risco"
    __tablename__ = "sst_condicao_fator_risco"
    empresa = models.ForeignKey(Empresa, null=False, on_delete=models.PROTECT, verbose_name="Empresa")
    funcionario = models.ForeignKey(Funcionario, null=False, on_delete=models.PROTECT, verbose_name="Funcionário")
    data_inicio = models.DateField(null=False, verbose_name="Data de início")
    descricao_atividade_ambiente = models.CharField(max_length=1000, null=True, verbose_name="Descrição das atividades desempenhadas no trabalho")
    atividades = models.ManyToManyField(Atividade, verbose_name="Atividades")
    responsavel_registro_ambiental = models.ForeignKey(ResponsavelRegistroAmbiental, on_delete=models.PROTECT, null=True)
    metodologia_riscos_ergonomicos = models.CharField(max_length=1000, null=True)
    observacao = models.CharField(max_length=1000, null=True)
    cadastro_completo = models.BooleanField(null=False, default=False)

class CondicaoFator(models.Model):
    fator_risco = models.ForeignKey(FatorRisco, on_delete=models.PROTECT, verbose_name="Fator de risco")
    tipo_avaliacao = models.IntegerField(choices=get_choices(CriterioAvaliacao), null=False, verbose_name="Tipo de avaliação")
    intensidade = models.IntegerField(null=False, verbose_name="Intensidade")
    limite_tolerancia = models.IntegerField(null=True, verbose_name="Limite de tolerância") #tem coisa errada
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT, verbose_name="Unidade de medida")
    tecnica_utilizada = models.CharField(max_length=1000, null=False, verbose_name="Técnica utilizada")
    insalubridade = models.BooleanField(default=False, null=False, verbose_name="Insalubridade")
    periculosidade = models.BooleanField(default=False, null=False, verbose_name="Periculosidade")
    aposentadoria_especial = models.BooleanField(default=False, null=False, verbose_name="Aposentadoria especial")
    utilizacao_epc = models.IntegerField(choices=get_choices(UtilizacaoEPC), null=False, verbose_name="Utilização de EPC")
    epc_eficaz = models.BooleanField(null=False, default=False, verbose_name="EPC eficaz")
    utilizacao_epi = models.IntegerField(choices=get_choices(UtilizacaoEPI), null=False, verbose_name="Utilização de EPI")
    condicao_ambiental_fator_risco = models.ForeignKey(CondicaoAmbientalFatorRisco, on_delete=models.PROTECT, null=True)

class AnaliseEPI(models.Model):
    __tablename__ = "sst_analise_epi"
    class Meta:
        verbose_name="Análise de EPI"
        verbose_name_plural="Análises de EPI"
    certificacao_epi = models.CharField(max_length=200, null=True, verbose_name="Certificação do EPI")
    descricao_epi = models.CharField(max_length=1500, null=True, verbose_name="Descrição do EPI")
    epi_eficaz = models.BooleanField(null=False, default=False, verbose_name="EPI eficaz")
    hierarquia_medida_protecao_coletiva = models.BooleanField(null=False, default=False, verbose_name="Hierarquia das medidas de proteção coletiva")
    observada_condicao_funcionamento = models.BooleanField(null=False, default=False, verbose_name="Observadas as condições de funcionamento")
    observado_epi = models.BooleanField(null=False, default=False, verbose_name="Observada uso da EPI")
    observado_prazo_validade_ca = models.BooleanField(null=False, default=False, verbose_name="Observada o prazo de validade do CA")
    observado_periodicidade_troca = models.BooleanField(null=False, default=False, verbose_name="Observada a periodicidade de troca")
    observada_higienizacao_epi = models.BooleanField(null=False, default=False, verbose_name="Observada higienização da EPI")
    condicao_fator = models.ForeignKey(CondicaoFator, on_delete=models.PROTECT, null=True)
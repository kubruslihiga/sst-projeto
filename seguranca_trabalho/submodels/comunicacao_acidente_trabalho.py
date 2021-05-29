from django.db import models
from typing import Any, List, Tuple
from seguranca_trabalho.submodels.funcionario import Funcionario
from seguranca_trabalho.submodels.empresa import Empresa

def get_choices(constant_clazz: Any) -> List[Tuple[str, Any]]:
    return [(value, value) for key, value in vars(constant_clazz).items() if not key.startswith('__')]

class ClassificacaoMedica:
    CRM = 1
    CRO = 2
    RMS = 3
    NONE = None

class LadoCorpoAtingido:
    NAO_APLICA = 0
    ESQUERDA = 1
    DIREITA = 2
    AMBAS = 3
    NONE = None

class TipoInscricao:
    CNPJ = 1
    CAEPF = 2
    CNO = 4
    NONE = None

class AvisoComunicacaoAcidente:
    INICIATIVA_EMPREGADOR = 1
    ORDEM_JUDICIAL = 2
    DETERMINACAO_ORGAO_FISCALIZADOR = 3
    NONE = None

class TipoCAT:
    INICIAL = 1
    REABERTURA = 2
    COMUNICACAO_OBITO = 3
    NONE = None

class TipoLocalizacao:
    ESTABELECIMENTO_BRASIL = 1
    ESTABELECIMENTO_EXTERIOR = 2
    ESTABELECIMENTO_TERCEIROS = 3
    VIA_PUBLICA = 4
    AREA_RURAL = 5
    EMBARCACAO = 6
    OUTROS = 9
    NONE = None

class TipoAcidente(models.Model):
    __tablename__ = "sst_tipo_acidente"
    class Meta:
        verbose_name="Tipo de acidente"
        verbose_name_plural="Tipos de acidentes"
    codigo = models.CharField(max_length=10, null=False, verbose_name="Código")
    descricao = models.CharField(max_length=500, null=True, verbose_name="Descriçao")
    def __str__(self):
        return self.codigo + " - " + self.descricao

class FatorAcidente(models.Model):
    __tablename__ = "sst_fator_acidente"
    class Meta:
        verbose_name="Fator acidente"
        verbose_name_plural="Fatores acidente"
    codigo = models.CharField(max_length=10, null=False, verbose_name="Código")
    descricao = models.CharField(max_length=500, null=True, verbose_name="Descriçao")
    def __str__(self):
        return self.codigo + " - " + self.descricao

class ParteCorpoAtingida(models.Model):
    __tablename__ = "sst_parte_corpo_atingida"
    class Meta:
        verbose_name="Parte corpo atingida"
        verbose_name_plural="Partes corpo atingida"
    codigo = models.CharField(max_length=15, null=True, verbose_name="Código")
    descricao = models.CharField(max_length=500, null=True, verbose_name="Descriçao")
    def __str__(self):
        return self.codigo + " - " + self.descricao

class NaturezaLesao(models.Model):
    class Meta:
        verbose_name="Natureza lesão"
        verbose_name_plural="Naturezas lesões"
    __tablename__ = "sst_natureza_lesao"
    codigo = models.CharField(max_length=15, null=True, verbose_name="Código")
    descricao = models.CharField(max_length=750, null=True, verbose_name="Descriçao")
    def __str__(self):
        return self.codigo + " - " + self.descricao

class AgenteCausadorAcidenteTrabalho(models.Model):
    class Meta:
        verbose_name="Agente causador do acidente de trabalho"
        verbose_name_plural="Agentes causadores do acidente de trabalho"
    codigo = models.CharField(max_length=15, null=True, verbose_name="Código")
    descricao = models.CharField(max_length=1000, null=True, verbose_name="Descriçao")
    def __str__(self):
        return self.codigo + " - " + self.descricao

class ComunicacaoAcidenteTrabalho(models.Model):
    class Meta:
        verbose_name="Comunicação de acidente do trabalho"
        verbose_name_plural="Comunicações de acidente do trabalho"
    __tablename__ = "sst_cat"
    empresa = models.ForeignKey(Empresa, null=False, on_delete=models.PROTECT, verbose_name="Empresa")
    funcionario = models.ForeignKey(Funcionario, null=False, on_delete=models.PROTECT, verbose_name="Funcionário")
    acidente_data_hora = models.DateTimeField(null=False, verbose_name="Data/hora do acidente")
    tipo_acidente = models.ForeignKey(TipoAcidente, null=False, on_delete=models.PROTECT, verbose_name="Tipo do acidente")
    tipo_cat = models.IntegerField(choices=get_choices(TipoCAT), null=True, verbose_name="Tipo da CAT")
    acidente_horas_trabalhadas = models.PositiveIntegerField(null=False, verbose_name="Horas trabalhadas até o momento do acidente")
    acidente_obito = models.BooleanField(null=False, default=False, verbose_name="Acidente com óbito")
    acidente_data_obito = models.DateTimeField(null=True, verbose_name="Data/hora do óbito")
    acidente_notificacao_policial = models.BooleanField(null=False, default=False, verbose_name="Notificação policial")
    fator_acidente = models.ForeignKey(FatorAcidente, null=False, on_delete=models.PROTECT, verbose_name="Fator do acidente")
    acidente_aviso_comunicacao = models.IntegerField(choices=get_choices(AvisoComunicacaoAcidente), null=False, verbose_name="Comunicação do acidente")
    observacao = models.CharField(max_length=1000, null=True, verbose_name="Observação")
    tipo_localizacao_acidente = models.IntegerField(choices=get_choices(TipoLocalizacao), null=False, verbose_name="Tipo do local do acidente")
    #ambiente_trabalho = models.ForeignKey(AmbienteTrabalho, null=False, on_delete=models.PROTECT)
    localizacao_acidente_especificacao = models.CharField(max_length=1000, null=False, verbose_name="Especificação do local do acidente")
    acidente_tipo_endereco = models.CharField(max_length=30, null=False, verbose_name="Tipo do endereço")
    acidente_endereco_descricao = models.CharField(max_length=1000, null=False, verbose_name="Endereço")
    acidente_endereco_numero = models.PositiveIntegerField(null=False, verbose_name="Número")
    acidente_endereco_complemento = models.CharField(max_length=500, null=False, verbose_name="Complemento")
    acidente_endereco_bairro = models.CharField(max_length=500, null=False, verbose_name="Bairro")
    acidente_endereco_cep = models.CharField(max_length=100, null=False, verbose_name="CEP")
    acidente_endereco_cidade = models.CharField(max_length=200, null=False, verbose_name="Cidade")
    acidente_endereco_estado = models.CharField(max_length=200, null=False, verbose_name="UF")
    acidente_endereco_pais = models.CharField(max_length=100, null=False, verbose_name="País")
    acidente_endereco_codigo_postal = models.CharField(max_length=100, null=False, verbose_name="Código postal")
    tipo_inscricao = models.IntegerField(choices=get_choices(TipoInscricao), null=False, verbose_name="Tipo de inscrição")
    inscricao_numero = models.CharField(max_length=100, null=False, verbose_name="Número da inscrição")
    parte_corpo_atingida = models.ManyToManyField(ParteCorpoAtingida, verbose_name="Parte do corpo atingida")
    lado_parte_corpo_atingida = models.IntegerField(choices=get_choices(LadoCorpoAtingido), null=False, verbose_name="Lado do corpo atingida")
    atestado_medico_codigo = models.CharField(max_length=100, null=False, verbose_name="Código do atestado médico")
    atestado_medico_data = models.DateTimeField(null=False, verbose_name="Data/hora do atestado médico")
    internacao = models.BooleanField(null=False, default=False, verbose_name="Internação")
    tempo_internacao = models.PositiveIntegerField(null=True, verbose_name="Tempo de hospitalização", help_text="Tempo em dias")
    afastamento_medico = models.BooleanField(null=False, default=False, verbose_name="Afastamento médico")
    natureza_lesao = models.ForeignKey(NaturezaLesao, null=False, on_delete=models.PROTECT, verbose_name="Natureza da lesão")
    lesao_complemento_descricao = models.CharField(max_length=2000, null=False, verbose_name="Descrição complementar da lesão")
    diagnostico = models.CharField(max_length=2000, null=False, verbose_name="Provável diagnóstico médico")
    cid_codigo = models.CharField(max_length=50, null=False, verbose_name="Código CID")
    atestado_medico_observacao = models.CharField(max_length=2000, null=True, verbose_name="Observação médica")
    nome_medico = models.CharField(max_length=150, null=False, verbose_name="Nome do profissional da saúde")
    classificao_codigo_medico = models.IntegerField(choices=get_choices(ClassificacaoMedica), null=False, verbose_name="Órgão de classe")
    numero_inscricao_medica = models.CharField(max_length=20, null=False, verbose_name="Número de inscrição")
    uf_medico = models.CharField(max_length=100, null=False, verbose_name="UF")
    agentes_causadores = models.ManyToManyField(AgenteCausadorAcidenteTrabalho, verbose_name="Agentes causadores do acidente de trabalho")
    codigo_cat = models.CharField(max_length=100, null=True, verbose_name="Código CAT")
    e_social_notificado = models.BooleanField(null=False, default=False, verbose_name="CAT informada ao E-SOCIAL")
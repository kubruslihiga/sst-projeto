from django.db import models
from typing import Any, List, Tuple

def get_choices(constant_clazz: Any) -> List[Tuple[str, Any]]:
    return [(value, value) for key, value in vars(constant_clazz).items() if not key.startswith('__')]

class ClassificacaoMedica:
    CRM = 1
    CRO = 2
    RMS = 3

class LadoCorpoAtingido:
    NAO_APLICA = 0
    ESQUERDA = 1
    DIREITA = 2
    AMBAS = 3

class TipoInscricao:
    CNPJ = 1
    CAEPF = 2
    CNO = 4

class AvisoComunicacaoAcidente:
    INICIATIVA_EMPREGADOR = 1
    ORDEM_JUDICIAL = 2
    DETERMINACAO_ORGAO_FISCALIZADOR = 3

class TipoCAT:
    INICIAL = 1
    REABERTURA = 2
    COMUNICACAO_OBITO = 3

class TipoLocalizacao:
    ESTABELECIMENTO_BRASIL = 1
    ESTABELECIMENTO_EXTERIOR = 2
    ESTABELECIMENTO_TERCEIROS = 3
    VIA_PUBLICA = 4
    AREA_RURAL = 5
    EMBARCACAO = 6
    OUTROS = 9

class TipoAcidente(models.Model):
    __tablename__ = "sst_tipo_acidente"
    class Meta:
        verbose_name="Tipo de acidente"
        verbose_name_plural="Tipos de acidentes"
    codigo = models.CharField(max_length=10, null=False)
    descricao = models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.codigo + " - " + self.descricao

class FatorAcidente(models.Model):
    __tablename__ = "sst_fator_acidente"
    class Meta:
        verbose_name="Fator acidente"
        verbose_name_plural="Fatores acidente"
    codigo = models.CharField(max_length=10, null=False)
    descricao = models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.codigo + " - " + self.descricao

class ParteCorpoAtingida(models.Model):
    __tablename__ = "sst_parte_corpo_atingida"
    class Meta:
        verbose_name="Parte corpo atingida"
        verbose_name_plural="Partes corpo atingida"
    codigo = models.CharField(max_length=15, null=True)
    descricao = models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.codigo + " - " + self.descricao

class NaturezaLesao(models.Model):
    class Meta:
        verbose_name="Natureza lesão"
        verbose_name_plural="Naturezas lesões"
    __tablename__ = "sst_natureza_lesao"
    codigo = models.CharField(max_length=15, null=True)
    descricao = models.CharField(max_length=750, null=True)
    def __str__(self):
        return self.codigo + " - " + self.descricao
    
#sst_cat_parte_corpo = Table('sst_cat_parte_corpo', models.Model.metadata,
#    Column('cat_id', Integer, ForeignKey('sst_cat.id')),
#    Column('parte_corpo_atingida', Integer, ForeignKey('sst_parte_corpo_atingida.id'))
#)

class ComunicacaoAcidenteTrabalho(models.Model):
    class Meta:
        verbose_name="Comunicação de acidente do trabalho"
        verbose_name_plural="Comunicações de acidente do trabalho"
    __tablename__ = "sst_cat"
    # funcionario = relationship("Funcionario")
    #(Integer, ForeignKey('sst_funcionario.id'), comment="Id do funcionario", doc="Id do funcionario")
    funcionario_id = models.IntegerField(null=True)
    #empresa = relationship("Empresa")
    # Integer, ForeignKey('sst_empresa.id'), comment="Id da empresa", doc="Id da empresa"
    empresa_id = models.IntegerField(null=False)
    acidente_data_hora = models.DateTimeField(null=False)
    tipo_acidente = models.ForeignKey(TipoAcidente, null=False, on_delete=models.PROTECT)
    tipo_cat = models.IntegerField(choices=get_choices(TipoCAT), null=True)
    acidente_horas_trabalhadas = models.TimeField(null=False)
    acidente_obito = models.BooleanField(null=False, default=False)
    acidente_data_obito = models.DateTimeField(null=True)
    acidente_notificacao_policial = models.BooleanField(null=False, default=False)
    fator_acidente = models.ForeignKey(FatorAcidente, null=False, on_delete=models.PROTECT)
    acidente_aviso_comunicacao = models.IntegerField(choices=get_choices(AvisoComunicacaoAcidente), null=False)
    observacao = models.CharField(max_length=1000, null=True)
    tipo_localizacao_acidente = models.IntegerField(choices=get_choices(TipoLocalizacao), null=False)
    #ambiente_trabalho = models.ForeignKey(AmbienteTrabalho, null=False, on_delete=models.PROTECT)
    localizacao_acidente_especificacao = models.CharField(max_length=1000, null=False)
    acidente_tipo_endereco = models.CharField(max_length=30, null=False)
    acidente_endereco_descricao = models.CharField(max_length=1000, null=False)
    acidente_endereco_numero = models.IntegerField(null=False)
    acidente_endereco_complemento = models.CharField(max_length=500, null=False)
    acidente_endereco_bairro = models.CharField(max_length=500, null=False)
    acidente_endereco_cep = models.CharField(max_length=100, null=False)
    acidente_endereco_cidade = models.CharField(max_length=200, null=False)
    acidente_endereco_estado = models.CharField(max_length=200, null=False)
    acidente_endereco_pais = models.CharField(max_length=100, null=False)
    acidente_endereco_codigo_postal = models.CharField(max_length=100, null=False)
    tipo_inscricao = models.IntegerField(choices=get_choices(TipoInscricao), null=False)
    inscricao_numero = models.CharField(max_length=100, null=False)
    parte_corpo_atingida = models.ManyToManyField(ParteCorpoAtingida)
    lado_parte_corpo_atingida = models.IntegerField(choices=get_choices(LadoCorpoAtingido), null=False)
    atestado_medico_codigo = models.CharField(max_length=100, null=False)
    atestado_medico_data = models.DateTimeField(null=False)
    hospital = models.BooleanField(null=False, default=False)
    tempo_hospital = models.IntegerField(null=True)
    afastamento_medico = models.BooleanField(null=False, default=False)
    natureza_lesao = models.ForeignKey(NaturezaLesao, null=False, on_delete=models.PROTECT)
    lesao_complemento_descricao = models.CharField(max_length=2000, null=False)
    diagnostico = models.CharField(max_length=2000, null=False)
    cid_codigo = models.CharField(max_length=50, null=False)
    atestado_medico_observacao = models.CharField(max_length=2000, null=True)
    nome_medico = models.CharField(max_length=150, null=False)
    natureza_lesao_classificao = models.IntegerField(choices=get_choices(ClassificacaoMedica), null=False)
    classificao_codigo_medico = models.CharField(max_length=150, null=False)
    uf_medico = models.CharField(max_length=100, null=False)
    #agente causador!
    codigo_cat = models.CharField(max_length=100, null=True)
    e_social_notificado = models.BooleanField(null=False, default=False)
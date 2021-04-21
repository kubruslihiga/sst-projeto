from sqlalchemy import Column, Integer, String, Sequence, DateTime, Enum, Boolean, ForeignKey, Table, Time, Date, Float
from sqlalchemy.orm import relationship
from ..database import Base
import enum

class TabelaESocial(enum.Enum):
    S2245='S2245'
    S2240='S2240'
    S2220='S2220'
    S1060='S1060'
    S2210='S2210'

class EnvioESocial(Base):
    __tablename__ = "sst_envio_esocial"
    id = Column(Integer, Sequence('envio_esocial_id_sequence'), primary_key=True)
    empresa_id = Column(Integer, ForeignKey('sst_empresa.id'), comment="Id da empresa", doc="Id da empresa")
    tabela_esocial = Column(Enum(TabelaESocial), nullable=False)
    link_requisicao_body = Column(String(1500), nullable=True)
    cat_id = Column(Integer, ForeignKey('sst_cat.id'), comment="Id da CAT", doc="Id da CAT", nullable=True)
    condicao_fator_risco_id = Column(Integer, ForeignKey('sst_condicao_fator_risco.id'), comment="Id da tabela condicao fator risco", doc="Id da tabela condicao fator risco", nullable=True)
    ambiente_trabalho_id = Column(Integer, ForeignKey('sst_ambiente_trabalho.id'), comment="Id do ambiente trabalho", doc="Id do ambiente trabalho", nullable=True)
    monitoramento_saude_id = Column(Integer, ForeignKey('sst_monitoramento_saude.id'), comment="Id do monitoramento saude do trabalhador", doc="Id do monitoramento saude do trabalhador", nullable=True)
    registro_capacitacao_id = Column(Integer, ForeignKey('sst_registro_capacitacao.id'), comment="Id do registro capacitacao do funcionario", doc="Id do registro capacitacao do funcionario", nullable=True)
    codigo_resposta_esocial = Column(String(10), nullable=True)
    resposta_sucesso = Column(Boolean, default=False,nullable=False)
    resposta_link = Column(String(1500), nullable=True)
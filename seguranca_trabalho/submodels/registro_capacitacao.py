from sqlalchemy import Column, Integer, String, Sequence, DateTime, Enum, Boolean, ForeignKey, Table, Time, Date, Float
from sqlalchemy.orm import relationship
from ..database import Base
import enum

class Treinamento(Base):
    __tablename__ = "sst_treinamento"
    id = Column(Integer, Sequence('treinamento_id_sequence'), primary_key=True)
    codigo = Column(String(20), nullable=False)
    descricao = Column(String(2000), nullable=False)
    categoria = Column(String(200), nullable=False)

class TipoTreinamento(enum.IntEnum):
    INICIAL=1
    PERIODICA = 2
    RECICLAGEM = 4
    OUTRO = 5

class ModalidadeTreinamento(enum.IntEnum):
    PRESENCIAL=1
    EAD=2
    MISTA=3

class VinculoProfissional(enum.IntEnum):
    PROFISSIONAL_VINCULADO=1
    SEM_VINCULO=2

class Nacionalidade(enum.IntEnum):
    BRASILEIRA=1
    ESTRANGEIRA=2

class ProfissionalCapacitacao(Base):
    __tablename__ = "sst_profissional_capacitacao"
    id = Column(Integer, Sequence('registro_capacitacao_id_sequence'), primary_key=True)
    cpf = Column(String(13), nullable=False)
    cbo = Column(String(20), nullable=False)
    nome = Column(String(150), nullable=False)
    vinculo_profissional = Column(Enum(VinculoProfissional), nullable=False)
    nacionalidade = Column(Enum(Nacionalidade), nullable=False)
    formacao_profissional = Column(String(300), nullable=False)

sst_registro_capacitacao_profissional = Table('sst_registro_capacitacao_profissional', Base.metadata,
    Column('registro_capacitacao_id', Integer, ForeignKey('sst_registro_capacitacao.id')),
    Column('profissional_capacitacao_id', Integer, ForeignKey('sst_profissional_capacitacao.id'))
)

class RegistroCapacitacao(Base):
    __tablename__ = "sst_registro_capacitacao"
    id = Column(Integer, Sequence('registro_capacitacao_id_sequence'), primary_key=True)
    funcionario = relationship("Funcionario")
    funcionario_id = Column(Integer, ForeignKey('sst_funcionario.id'), comment="Id do funcionario", doc="Id do funcionario")
    empresa = relationship("Empresa")
    empresa_id = Column(Integer, ForeignKey('sst_empresa.id'), comment="Id da empresa", doc="Id da empresa")
    estagiario = Column(Boolean, default=False, nullable=False)
    treinamento = relationship("Treinamento")
    treinamento_id = Column(Integer, ForeignKey('sst_treinamento.id'), comment="Id do treinamento", doc="Id do treinamento")
    observacao = Column(String(2000), nullable=False)
    data_inicio = Column(DateTime, nullable=False)
    duracao_horas = Column(Float, nullable=False)
    tipo = Column(Enum(TipoTreinamento), nullable=False)
    modalidade = Column(Enum(ModalidadeTreinamento), nullable=False)
    realizado_outro_empregado = Column(Boolean, default=False, nullable=False)
    profissionais_capacitacao = relationship('ProfissionalCapacitacao', secondary=sst_registro_capacitacao_profissional)
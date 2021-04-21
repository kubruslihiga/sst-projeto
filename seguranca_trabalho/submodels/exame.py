from sqlalchemy import Column, Integer, String, Sequence, DateTime, Enum, Boolean, ForeignKey, Table, Time, Date
from sqlalchemy.orm import relationship
from ..database import Base
import enum

class Diagnostico(Base):
    __tablename__="sst_diagnostico"
    id = Column(Integer, Sequence('diagnostico_id_sequence'), primary_key=True)
    codigo = Column(String(50), nullable=False)
    descricao = Column(String(1000), nullable=False)

class ExameDiagnostico(Base):
    __tablename__ = "sst_exame_diagnostico"
    exame_id = Column(Integer, ForeignKey("sst_exame.id"), primary_key=True)
    diagnostico_id = Column(Integer, ForeignKey("sst_diagnostico.id"), primary_key=True)

class Exame(Base):
    __tablename__= "sst_exame"
    id = Column(Integer, Sequence('exame_id_sequence'), primary_key=True)
    empresa = relationship("Empresa")
    empresa_id = Column(Integer, ForeignKey('sst_empresa.id'), comment="Id da empresa", doc="Id da empresa")
    matricula_sistema = Column(String(100), nullable=False, comment="Matricula sistema")
    diagnosticos = relationship(Diagnostico, secondary="sst_exame_diagnostico")
    validade_mensal = Column(Integer, nullable=False)
    observacao = Column(String(1000), nullable=True)

class FuncionarioExame(Base):
    __tablename__ = "sst_funcionario_exame"
    id = Column(Integer, Sequence('funcionario_exame_id_sequence'), primary_key=True)
    funcionario = relationship("Funcionario")
    funcionario_id = Column(Integer, ForeignKey('sst_funcionario.id'), comment="Id do funcionario", doc="Id do funcionario")
    empresa = relationship("Empresa")
    empresa_id = Column(Integer, ForeignKey('sst_empresa.id'), comment="Id da empresa", doc="Id da empresa")
    matricula_sistema = Column(String(100), nullable=False, comment="Matricula sistema")
    codigo_medico = Column(String(100), nullable=False, comment="Codigo medico")
    codigo_laboratorio = Column(String(100), nullable=False, comment="Codigo laboratorio")
    codigo_exame = Column(String(100), nullable=False, comment="Codigo exame")
    data_entraga = Column(Date, nullable=False, comment="Data entrega")
    data_validade = Column(Date, nullable=False, comment="Data validade")
    resultado = Column(String(255), nullable=False, comment="Resultado dos exames")
    observacao = Column(String(1000), nullable=True)

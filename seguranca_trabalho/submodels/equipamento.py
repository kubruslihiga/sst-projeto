from django.db import models
from .empresa import Empresa
from .funcionario import Funcionario
from .enums import get_choices, TipoEquipamento
from datetime import datetime

class Equipamento(models.Model):
    __tablename__ = "sst_equipamento"
    # id = models.IntegerField(Sequence('equipamento_id_sequence'), primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length=150, null=False)
    tipo = models.IntegerField(choices=get_choices(TipoEquipamento), null=False)
    hierarquia_protecao_coletiva = models.CharField(max_length=150, null=False)
    prazo_validade = models.DateTimeField(null=False)
    certificado_aprovacao = models.CharField(max_length=100, null=False)
    url_foto = models.CharField(max_length=1000, null=False)
    comentario = models.CharField(max_length=500, null=True)

class FuncionarioEquipamento(models.Model):
    __tablename__ = "sst_funcionario_equipamento"
    # id = models.IntegerField(Sequence('func_equi_id_sequence'), primary_key=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)
    quantidade = models.IntegerField(null=False)
    data_entrega = models.DateTimeField(null=False)
    devolucao = models.BooleanField(null=False, default=False)
    data_devolucao = models.DateTimeField(null=False, default=datetime.utcnow)
    data_vencimento = models.DateTimeField(null=False, default=datetime.utcnow)
    comentario = models.CharField(max_length=500, null=True)

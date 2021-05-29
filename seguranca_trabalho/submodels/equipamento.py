from django.db import models
from .empresa import Empresa
from .funcionario import Funcionario
from .enums import get_choices, TipoEquipamento
from datetime import datetime

class Equipamento(models.Model):
    __tablename__ = "sst_equipamento"
    # id = models.IntegerField(Sequence('equipamento_id_sequence'), primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, verbose_name="Empresa")
    codigo = models.CharField(max_length=50, null=False, verbose_name="Código")
    descricao = models.CharField(max_length=150, null=False, verbose_name="Descrição")
    tipo = models.IntegerField(choices=get_choices(TipoEquipamento), null=False, verbose_name="Tipo")
    hierarquia_protecao_coletiva = models.CharField(max_length=150, null=False, verbose_name="Hierarquia de proteção coletiva")
    prazo_validade = models.DateTimeField(null=False, verbose_name="Prazo de validade")
    certificado_aprovacao = models.CharField(max_length=100, null=False, verbose_name="Certificado de aprovação")
    url_foto = models.CharField(max_length=1000, null=False, verbose_name="Foto")
    comentario = models.CharField(max_length=500, null=True, verbose_name="Comentário")
    def __str__(self):
        return self.codigo + " - " + self.descricao

class FuncionarioEquipamento(models.Model):
    __tablename__ = "sst_funcionario_equipamento"
    # id = models.IntegerField(Sequence('func_equi_id_sequence'), primary_key=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name="Funcionário")
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, verbose_name="Empresa")
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT, verbose_name="Equipamento")
    quantidade = models.IntegerField(null=False, verbose_name="Quantidade")
    data_entrega = models.DateTimeField(null=False, verbose_name="Data de entrega")
    devolucao = models.BooleanField(null=False, default=False, verbose_name="Devolução")
    data_devolucao = models.DateTimeField(null=True, default=datetime.utcnow, verbose_name="Data de devolução")
    data_vencimento = models.DateTimeField(null=False, default=datetime.utcnow, verbose_name="Data de vencimento")
    comentario = models.CharField(max_length=500, null=True, verbose_name="Comentário")
    def __str__(self):
        return self.funcionario + " - " + self.equipamento

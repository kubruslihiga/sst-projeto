from django.db import models

class Empresa(models.Model):
    class Meta:
        verbose_name="Empresa"
        verbose_name_plural="Empresas"
    __tablename__="sst_empresa"
    codigo = models.CharField(max_length=20, null=False)
    cnpj = models.CharField(max_length=15, null=False)
    razao_social = models.CharField(max_length=150, null=False) # razao social
    nome_fantasia = models.CharField(max_length=150, null=False) # nome fantasia
    inscricao_estadual = models.CharField(max_length=30, null=False) # inscricao estadual
    inscricao_municipal = models.CharField(max_length=30, null=False) # inscricao municipal
    endereco = models.CharField(max_length=250, null=False) # endereco
    cidade = models.CharField(max_length=80, null=False) # cidade
    numero = models.CharField(max_length=20, null=False) # numero
    complemento = models.CharField(max_length=150, null=True) # complemento
    cep = models.CharField(max_length=20, null=False) # CEP
    cnae = models.CharField(max_length=20, null=False) # CNAE

    def __str__(self):
        return self.codigo + ": " + self.razao_social
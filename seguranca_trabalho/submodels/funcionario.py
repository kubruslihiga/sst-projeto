from django.db import models
from .enums import Genero, get_choices
from .empresa import Empresa

class ClassificacaoBrasileiraOcupacao(models.Model):
    class Meta:
        verbose_name="Classificação brasileira de ocupação"
        verbose_name_plural="Classificações brasileira de ocupação"
    codigo = models.CharField(max_length=100, null=False, verbose_name="Código")
    descricao = models.CharField(max_length=300, null=False, verbose_name="Descrição")

    def __str__(self):
        return self.codigo + " - " + self.descricao

class Setor(models.Model):
    class Meta:
        verbose_name="Setor"
        verbose_name_plural="Setores"
    codigo = models.CharField(max_length=100, null=False, verbose_name="Código")
    descricao = models.CharField(max_length=300, null=False, verbose_name="Descrição")
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.codigo + " - " + self.descricao

class Cargo(models.Model):
    class Meta:
        verbose_name="Cargo"
        verbose_name_plural="Cargos"
    codigo = models.CharField(max_length=100, null=False, verbose_name="Código")
    descricao = models.CharField(max_length=300, null=False, verbose_name="Descrição")
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.codigo + " - " + self.descricao

class Funcao(models.Model):
    class Meta:
        verbose_name="Função"
        verbose_name_plural="Funções"
    codigo = models.CharField(max_length=100, null=False, verbose_name="Código")
    descricao = models.CharField(max_length=300, null=False, verbose_name="Descrição")
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.codigo + " - " + self.descricao

class Funcionario(models.Model):
    __tablename__= "sst_funcionario"
    class Meta:
        verbose_name="Funcionário"
        verbose_name_plural="Funcionários"
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=False)
    codigo_erp = models.CharField(max_length=100, null=False, help_text="Código cadastrado nos sistemas de informação da empresa", verbose_name="Código ERP")
    codigo_esocial = models.CharField(max_length=100, null=False, help_text="Código no E-SOCIAL", verbose_name="Código no E-SOCIAL")
    nome = models.CharField(max_length=100, null=False, verbose_name="Nome")
    genero = models.IntegerField(choices=get_choices(Genero), null=False, verbose_name="Gênero")
    cbo = models.ForeignKey(ClassificacaoBrasileiraOcupacao, null=True, on_delete=models.PROTECT, verbose_name="CBO", help_text="Classificação brasileira de ocupação")
    cpf = models.CharField(max_length=13, null=False, verbose_name="CPF")
    rg = models.CharField(max_length=15, null=False, verbose_name="RG")
    nis = models.CharField(max_length=20, null=True, verbose_name="NIS")
    pis = models.CharField(max_length=20, null=True, verbose_name="PIS")
    pasep = models.CharField(max_length=20, null=True, verbose_name="PASEP")
    nit = models.CharField(max_length=20, null=True, verbose_name="NIT")
    data_nascimento = models.DateField(null=False, verbose_name="Data de nascimento")
    estagiario = models.BooleanField(default=False)
    data_exame_admissional = models.DateTimeField(null=False, verbose_name="Data do exame admissional")
    data_exame_demissional = models.DateTimeField(null=True, verbose_name="Data do exame demissional", help_text="Campo não obrigatório para funcionário ativo")
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, null=True)
    funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT, null=True)
    url_imagem = models.CharField(max_length=1000, null=True, verbose_name="URL da imagem")

    def __str__(self):
        return self.nome

"""class FuncionarioSchema(BaseModel):
    id: Optional[int]
    codigo_empresa: str
    codigo_erp: constr(max_length=100)
    codigo_esocial: constr(max_length=100)
    nome: constr(max_length=100)
    genero: Genero
    cbo: constr(max_length=50)
    cpf: constr(max_length=13)
    rg: constr(max_length=15)
    nis: constr(max_length=20)
    pis: constr(max_length=20)
    pasep: constr(max_length=20)
    nit: constr(max_length=20)
    data_nascimento: str
    estagiario: bool
    data_exame_admissional: Optional[str]
    data_exame_demissional: Optional[str]
    setor: constr(max_length=50)
    cargo: constr(max_length=50)
    funcao: constr(max_length=50)
    url_imagem: constr(max_length=1000)

    @validator('data_nascimento')
    def validador_data_nascimento(cls, v):
        try:
            return datetime.strptime(v, '%d/%m/%Y')
        except ValueError:
            return v

    @validator('data_exame_demissional')
    def validador_data_demissional(cls, v):
        try:
            return datetime.strptime(v, "%d/%m/%Y %H:%M:%S")
        except ValueError:
            return v
    
    @validator('data_exame_admissional')
    def validador_data_admissional(cls, v):
        try:
            return datetime.strptime(v, '%d/%m/%Y %H:%M:%S')
        except ValueError:
            return v

    class Config:
        orm_mode = True"""
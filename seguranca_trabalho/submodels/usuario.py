import re
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core import validators

from .empresa import Empresa

class UsuarioManager(BaseUserManager):
    def _create_user(self, username, password, is_superuser, data_nascimento, empresas = [], **extra_fields):
        now = timezone.now()
        if not username:
          raise ValueError(_('Username must be set'))
        #email = self.normalize_email(email)
        usuario = self.model(username=username, data_nascimento=data_nascimento,
            is_superuser=is_superuser, last_login=now, **extra_fields)
        usuario.is_staff = True
        usuario.is_active=True
        usuario.date_joined = now
        usuario.set_password(password)
        usuario.save(using=self._db)
        if empresas:
            usuario.empresas.set(empresas)
            usuario.save(using=self._db)
        return usuario

    def create_user(self, username=None, password=None, **extra_fields):
        now = timezone.now()
        empresas = []
        return self._create_user(username, password, False, now, empresas, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        now = timezone.now()
        empresas = []
        user=self._create_user(username, password, True, now, empresas, **extra_fields)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, default="default username", unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    email = models.EmailField(_('email address'), unique=True)
    nome_completo = models.CharField("Nome completo", max_length=150, null=True)
    data_nascimento = models.DateField(null=True, blank=True)
    empresa_selecionada = models.ForeignKey(Empresa, null=True, on_delete=models.PROTECT, blank=True)
    empresas = models.ManyToManyField(Empresa, verbose_name="Empresas", blank=True, related_name="empresa_set", related_query_name="empresas",)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UsuarioManager()

    def __str__(self):
        return 'Vazio' if not self.nome_completo else self.nome_completo

    class Meta:
        verbose_name="Usuário"
        verbose_name_plural="Usuários"

"""class NivelUsuario(enum.IntEnum):
    ADMIN = 0,
    USUARIO = 1

class PermissaoSchema(BaseModel):
    id: Optional[int]
    codigo: constr(max_length=100)
    descricao: constr(max_length=1000)

class PerfilSchema(BaseModel):
    id: Optional[int]
    codigo: constr(max_length=100)
    descricao: constr(max_length=1000)
    permissoes: List[PermissaoSchema] = []
    codigos_permissoes: Optional[Set[str]]

class UsuarioSchema(BaseModel):
    id: Optional[int]
    login: constr(max_length=100)
    nome: constr(max_length=100)
    email: constr(max_length=100)
    senha: Optional[str]
    receber_alertas: bool = False
    codigo_empresa: str
    perfis: List[PerfilSchema] = []
    data_cadastro: Optional[str]
    codigo_permissoes: Set[str] = []
    codigo_perfis: List[str] = []

class Permissao(Base):
    __tablename__= "sst_permissao"
    id = Column(Integer, Sequence('permissao_id_sequence'), primary_key=True)
    codigo = Column(String(100), nullable=False, comment="Codigo")
    descricao = Column(String(1000), nullable=False, comment="Descricao")

    def to_schema(self):
        data = {}
        if (self.id):
            data['id'] = self.id
        if (self.codigo):
            data['codigo'] = self.codigo
        if (self.descricao):
            data['descricao'] = self.descricao
        ret = PermissaoSchema(**data)
        return ret

sst_perfil_permissao = Table('sst_perfil_permissao', Base.metadata,
    Column('perfil_id', Integer, ForeignKey('sst_perfil.id')),
    Column('permissao_id', Integer, ForeignKey('sst_permissao.id'))
)

class Perfil(Base):
    __tablename__= "sst_perfil"
    id = Column(Integer, Sequence('perfil_id_sequence'), primary_key=True)
    codigo = Column(String(100), nullable=False, comment="Codigo")
    descricao = Column(String(1000), nullable=False, comment="Descricao")
    permissoes = relationship('Permissao', secondary=sst_perfil_permissao)
    def to_schema(self):
        data = {}
        if (self.id):
            data['id'] = self.id
        if (self.codigo):
            data['codigo'] = self.codigo
        if (self.descricao):
            data['descricao'] = self.descricao
        if (self.permissoes and len(self.permissoes) > 0):
            permissoes_schema = []
            codigos_permissoes = set()
            for p in self.permissoes:
                permissoes_schema.append(p.to_schema())
                codigos_permissoes.add(p.codigo)
            data['codigos_permissoes'] = codigos_permissoes
            data['permissoes'] = permissoes_schema
        ret = PerfilSchema(**data)
        return ret

sst_usuario_perfil = Table('sst_usuario_perfil', Base.metadata,
    Column('perfil_id', Integer, ForeignKey('sst_perfil.id')),
    Column('usuario_id', Integer, ForeignKey('sst_usuario.id'))
)

class Usuario(Base):
    __tablename__= "sst_usuario"
    id = Column(Integer, Sequence('usuario_id_sequence'), primary_key=True)
    login = Column(String(100), nullable=False, comment="Login")
    nome = Column(String(100), nullable=False, comment="Nome")
    email = Column(String(100), nullable=False, comment="Email")
    receber_alertas = Column(Boolean, nullable=False, default=False)
    perfis = relationship('Perfil', secondary=sst_usuario_perfil)
    empresa = relationship("Empresa")
    empresa_id = Column(Integer, ForeignKey('sst_empresa.id'), comment="Id da empresa", doc="Id da empresa", nullable=True)
    senha = Column(String(1024), nullable=False, comment="Senha")
    data_cadastro = Column(DateTime, nullable=False, comment="Data insercao usuario")

    def to_schema(self):
        data = {}
        if (self.id):
            data['id'] = self.id
        if (self.login):
            data['login'] = self.login
        if (self.nome):
            data['nome'] = self.nome
        if (self.email):
            data['email'] = self.email
        if (self.receber_alertas):
            data['receber_alertas'] = self.receber_alertas
        if (self.empresa):
            data['codigo_empresa'] = self.empresa.codigo
        if (self.data_cadastro):
            data['data_cadastro'] = self.data_cadastro.strftime("%d/%m/%Y %H:%M:%S")
        if (self.perfis and len(self.perfis) > 0):
            perfis_schema: list[PerfilSchema] = []
            perfis_cod_list = []
            permissao_cod_set = set()
            for perfil_model in self.perfis:
                p_schema = perfil_model.to_schema()
                perfis_schema.append(p_schema)
                perfis_cod_list.append(perfil_model.codigo)
                permissao_cod_set.update(p_schema.codigos_permissoes)
            data['codigo_permissoes'] = permissao_cod_set
            data['codigo_perfis'] = perfis_cod_list
            data['perfis'] = perfis_schema
        ret = UsuarioSchema(**data)
        return ret"""

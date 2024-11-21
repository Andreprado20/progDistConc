# coding: utf-8
from sqlalchemy import CheckConstraint, Column, DateTime, ForeignKey, Integer, Numeric, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Criptoativo(Base):
    __tablename__ = 'criptoativo'

    id = Column(Integer, primary_key=True, server_default=text("nextval('criptoativo_id_seq'::regclass)"))
    nome = Column(String(255), nullable=False, unique=True)
    codigo = Column(String(10), nullable=False)
    preco = Column(Numeric(30, 8), nullable=False)


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, server_default=text("nextval('usuario_id_seq'::regclass)"))
    nome = Column(String(255), nullable=False)
    login = Column(String(50), nullable=False, unique=True)
    senha = Column(String(20), nullable=False)


class Carteira(Base):
    __tablename__ = 'carteira'

    id = Column(Integer, primary_key=True, server_default=text("nextval('carteira_id_seq'::regclass)"))
    nome = Column(String(255), nullable=False)
    id_usuario = Column(ForeignKey('usuario.id', ondelete='CASCADE'), nullable=False)

    usuario = relationship('Usuario')


class CarteiraCripto(Base):
    __tablename__ = 'carteira_cripto'

    id_carteira = Column(ForeignKey('carteira.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    id_criptoativo = Column(ForeignKey('criptoativo.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    quantidade = Column(Numeric(30, 8), nullable=False, server_default=text("0"))

    carteira = relationship('Carteira')
    criptoativo = relationship('Criptoativo')


class Transacao(Base):
    __tablename__ = 'transacao'
    __table_args__ = (
        CheckConstraint("(tipo)::text = ANY ((ARRAY['compra'::character varying, 'venda'::character varying, 'transferencia'::character varying])::text[])"),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('transacao_id_seq'::regclass)"))
    id_carteira_origem = Column(ForeignKey('carteira.id', ondelete='SET NULL'), nullable=False)
    id_carteira_destino = Column(ForeignKey('carteira.id', ondelete='SET NULL'), nullable=False)
    id_criptoativo = Column(ForeignKey('criptoativo.id', ondelete='CASCADE'), nullable=False)
    quantidade = Column(Numeric(30, 8), nullable=False)
    tipo = Column(String(20), nullable=False)
    data = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    carteira = relationship('Carteira', primaryjoin='Transacao.id_carteira_destino == Carteira.id')
    carteira1 = relationship('Carteira', primaryjoin='Transacao.id_carteira_origem == Carteira.id')
    criptoativo = relationship('Criptoativo')

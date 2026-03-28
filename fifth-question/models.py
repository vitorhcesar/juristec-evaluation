from __future__ import annotations

from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(255))
    estado: Mapped[str] = mapped_column(String(255))

    processos: Mapped[list[Processo]] = relationship(back_populates="cliente")


class Processo(Base):
    __tablename__ = "processos"

    id_processo: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_cliente: Mapped[int] = mapped_column(
        ForeignKey("clientes.id_cliente"),
        nullable=False,
    )
    assunto: Mapped[str] = mapped_column(String(255))
    data_abertura: Mapped[date] = mapped_column(Date)

    cliente: Mapped[Cliente] = relationship(back_populates="processos")

from enum import Enum


class Papel(str, Enum):
    ATENDENTE = "ATEN                               DENTE"
    SOLICITANTE = "SOLICITANTE"


class StatusChamado(str, Enum):
    ABERTO = "ABERTO"
    EM_ANALISE = "EM_ANALISE"
    RESOLVIDO = "RESOLVIDO"
    CANCELADO = "CANCELADO"


class PrioridadeChamado(str, Enum):
    BAIXA = "BAIXA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"

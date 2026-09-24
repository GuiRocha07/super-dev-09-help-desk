export interface TicketResposta{
    id: number;
    numeroProtocolo: string;
    titulo: string;
    descricao: string;
    status: string;
    prioridade: string;
    setor: string;
    descricaoSolucao: string | null;
    motivoCancelamento: string | null;
    dataCriacao: Date;
    dataAtualizacao: Date | null;
    solicitanteId: number;
    atendenteId: number | null;
}

export interface TicketAssociar {
  idUsuario: number;
}

export interface TicketResolver {
  idUsuario: number;
  descricao: string;
}

export interface TicketCancelar {
  idUsuario: number;
  motivo: string;
}
import { HttpClient } from '@angular/common/http';
import { inject, Injectable, Service } from '@angular/core';
import { TicketResposta } from '../models/tickets.models';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TicketService {
  // HttpClient é o cliente que utilizamos no angular para fazer requests
  private http = inject(HttpClient);

  // URL do back-end por enquanto está fixo, depois
  // utilizaremos environment para ser dinâmico
  private baseUrl = `http://localhost:8000/tickets`;

  // função que será responsável por comunicar com o back
  // para obter a lista de tickets
  listar(): Observable<TicketResposta[]>{
    // faz a requisição para /tickets no back-end
    return this.http.get<TicketResposta[]>(this.baseUrl);
  }
}
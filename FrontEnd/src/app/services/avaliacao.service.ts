import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Avaliacao {
  id: number;
  texto: string;
  data: string; // Pode ser ajustado para Date, dependendo do uso
  id_usuario: number;
  id_produto: number;
}

@Injectable({
  providedIn: 'root'
})
export class AvaliacaoService {
  private apiUrl = 'http://localhost:5000/avaliacoes';
  private apiUrl2 = 'http://localhost:5000/avaliacao'; 

  constructor(private http: HttpClient) {}

  getAvaliacoes(): Observable<Avaliacao[]> {
    return this.http.get<Avaliacao[]>(this.apiUrl);
  }

  getAvaliacoesByProdutoId(id_produto: number): Observable<Avaliacao[]> {
    return this.http.get<Avaliacao[]>(`${this.apiUrl2}/${id_produto}`);
  }

  createAvaliacao(avaliacao: Partial<Avaliacao>): Observable<Avaliacao> {
    return this.http.post<Avaliacao>(`${this.apiUrl2}`, avaliacao);
  }
}

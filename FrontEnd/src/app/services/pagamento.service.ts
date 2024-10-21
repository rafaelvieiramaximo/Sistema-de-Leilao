import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Pagamento {
  id_usuario: number;
  id_produto: number;
  valor_total: number;
  forma_pagamento: string;
  status: string;
}

@Injectable({
  providedIn: 'root'
})
export class PagamentoService {
  private apiUrl = 'http://localhost:5000/pagamentos'; // URL da API
  private apiUrl2 = 'http://localhost:5000/pagamento'; // URL da API
  
  constructor(private http: HttpClient) { }

  getPagamentos(): Observable<Pagamento[]> {
    return this.http.get<Pagamento[]>(this.apiUrl);
  }

  addPagamento(pagamento: Pagamento): Observable<Pagamento> {
    return this.http.post<Pagamento>(this.apiUrl2, pagamento);
  }
}

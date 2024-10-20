import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Pagamento {
  id: number;
  valor: number;
  metodo: string;
  data: string; // Pode ser ajustado para Date, dependendo do uso
}

@Injectable({
  providedIn: 'root'
})
export class PagamentoService {
  private apiUrl = 'http://localhost:5000/pagamentos';

  constructor(private http: HttpClient) {}

  getPagamentos(): Observable<Pagamento[]> {
    return this.http.get<Pagamento[]>(this.apiUrl);
  }
}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Produto {
  id_produto: number;
  nome: string;
  descricao: string;
  preco_inicial: number;
  data_inicial: string;
  // Outros atributos que seu backend fornecer
}

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {
  private apiUrl = 'http://localhost:5000/produtos';
  private apiUrl2 = 'http://localhost:5000/produto'; 

  constructor(private http: HttpClient) {}

  getProdutos(): Observable<Produto[]> {
    return this.http.get<Produto[]>(this.apiUrl);
  }

  getProdutoById(id: number): Observable<Produto> {
    return this.http.get<Produto>(`${this.apiUrl2}/${id}`);
  }
}

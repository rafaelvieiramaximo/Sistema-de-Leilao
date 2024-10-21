import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Lance {
  id: number;
  valor: number;
  id_usuario: number;
  id_produto: number;
  data: string; // Pode ser ajustado para Date, dependendo do uso
}

@Injectable({
  providedIn: 'root',
})
export class LanceService {
  private apiUrl = 'http://localhost:5000/lances';
  private apiUrl2 = 'http://localhost:5000/lance';

  constructor(private http: HttpClient) {}

  getLances(): Observable<Lance[]> {
    return this.http.get<Lance[]>(this.apiUrl);
  }

  getLancesByProdutoId(id_produto: number): Observable<Lance[]> {
    return this.http.get<Lance[]>(`${this.apiUrl2}/${id_produto}`);
  }

  createLance(lance: Partial<Lance>): Observable<Lance> {
    return this.http.post<Lance>(`${this.apiUrl2}`, lance);
  }
}

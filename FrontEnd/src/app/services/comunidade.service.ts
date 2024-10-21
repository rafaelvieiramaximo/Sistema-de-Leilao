import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Comunidade {
  id: number;
  nome: string;
  descricao: string;
}

@Injectable({
  providedIn: 'root'
})
export class ComunidadeService {
  private apiUrl = 'http://localhost:5000/comunidades';

  constructor(private http: HttpClient) {}

  getComunidades(): Observable<Comunidade[]> {
    return this.http.get<Comunidade[]>(this.apiUrl);
  }
}
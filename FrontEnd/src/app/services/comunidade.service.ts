import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Comunidade {
  id_comunidade: number;
  nome: string;
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
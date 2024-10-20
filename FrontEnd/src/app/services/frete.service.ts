import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Frete {
  id: number;
  tipo: string;
  preco: number;
  tempo_estimado: string; // Pode ser ajustado para Date, dependendo do uso
}

@Injectable({
  providedIn: 'root'
})
export class FreteService {
  private apiUrl = 'http://localhost:5000/fretes';

  constructor(private http: HttpClient) {}

  getFretes(): Observable<Frete[]> {
    return this.http.get<Frete[]>(this.apiUrl);
  }
}

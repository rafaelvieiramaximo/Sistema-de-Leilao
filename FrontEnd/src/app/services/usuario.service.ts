import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export interface Usuario{
  id_usuario: number;
  nome: string;
  email: string;
  reputacao: number;
}

@Injectable({
  providedIn: 'root'
})

export class UsuarioService {

  private apiUrl = 'http://localhost:5000/usuarios';

  constructor(private http: HttpClient) { }

  getUsuarios(): Observable<Usuario[]> {
      return this.http.get<Usuario[]>(this.apiUrl);
  }
  delete(): Observable<void> {
      return this.http.delete<void>(`$http://localhost:5000//usuario/$int:id`);
  }
}

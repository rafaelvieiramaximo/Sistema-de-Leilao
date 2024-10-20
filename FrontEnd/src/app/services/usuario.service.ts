import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export interface Usuario {
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

  // Método para obter todos os usuários
  getUsuarios(): Observable<Usuario[]> {
    return this.http.get<Usuario[]>(this.apiUrl);
  }

  // Método para obter um usuário por ID
  getUsuarioById(id: number): Observable<Usuario> {
    return this.http.get<Usuario>(`http://localhost:5000/usuario/${id}`);
  }

  // Método para criar um novo usuário
  createUsuario(usuario: Partial<Usuario>): Observable<Usuario> {
    return this.http.post<Usuario>('http://localhost:5000/usuario', usuario);
  }

  // Método para editar um usuário existente por ID
  editUsuario(id: number, usuario: Partial<Usuario>): Observable<Usuario> {
    return this.http.put<Usuario>(`http://localhost:5000/usuario/${id}`, usuario);
  }

  // Método para deletar um usuário por ID
  delete(id: number): Observable<void> {
    return this.http.delete<void>(`http://localhost:5000/usuario/${id}`);
  }
}

import { Component } from '@angular/core';
import { Usuario, UsuarioService } from '../services/usuario.service';

@Component({
  selector: 'app-usuarios',
  templateUrl: './usuarios.component.html',
  styleUrl: './usuarios.component.css'
})
export class UsuariosComponent {
    usuarios: Usuario[] = [];
    
    constructor(private usuarioService: UsuarioService) {}

    ngOnInit(): void {
        this.usuarioService.getUsuarios().subscribe((data: Usuario[]) => {
          this.usuarios = data; 
        });
    }
}

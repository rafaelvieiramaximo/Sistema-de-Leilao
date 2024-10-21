import { Component } from '@angular/core';
import { Usuario, UsuarioService } from '../services/usuario.service';
import { Route, Router } from '@angular/router';

@Component({
  selector: 'app-usuarios',
  templateUrl: './usuarios.component.html',
  styleUrl: './usuarios.component.css'
})
export class UsuariosComponent {
    usuarios: Usuario[] = [];
    
    constructor(private usuarioService: UsuarioService, private router: Router) {}

    ngOnInit(): void {
        this.usuarioService.getUsuarios().subscribe((data: Usuario[]) => {
          this.usuarios = data; 
        });
    }

    route_produtos(){
      this.router.navigate(['/produtos']);
    }
}

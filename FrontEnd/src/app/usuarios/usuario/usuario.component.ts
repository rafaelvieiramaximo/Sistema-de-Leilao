import { Component, Input } from '@angular/core';
import { Usuario, UsuarioService } from '../../services/usuario.service';

@Component({
  selector: 'app-usuario',
  templateUrl: './usuario.component.html',
  styleUrl: './usuario.component.css'
})
export class UsuarioComponent {
  @Input() usuario!: Usuario;

  constructor(private usuarioService : UsuarioService){}

  delete(){
      this.usuarioService.delete();
  }

}
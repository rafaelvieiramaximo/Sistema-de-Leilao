import { Component, Input } from '@angular/core';
import { Usuario, UsuarioService } from '../../services/usuario.service';

@Component({
  selector: 'app-usuario',
  templateUrl: './usuario.component.html',
  styleUrls: ['./usuario.component.css'] // Corrigido: `styleUrl` para `styleUrls`
})
export class UsuarioComponent {
  @Input() usuario!: Usuario;

  constructor(private usuarioService: UsuarioService) {}

  // Método para deletar o usuário
  deleteUsuario() {
    if (this.usuario && this.usuario.id_usuario) {
      this.usuarioService.delete(this.usuario.id_usuario).subscribe(
        () => {
          console.log('Usuário deletado com sucesso.');
          // Aqui você pode adicionar código para remover o usuário da UI
        },
        error => {
          console.error('Erro ao deletar o usuário:', error);
        }
      );
    }
  }
}

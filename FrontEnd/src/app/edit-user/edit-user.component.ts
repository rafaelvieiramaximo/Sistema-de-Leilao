import { Component } from '@angular/core';
import { UsuarioService } from '../services/usuario.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-edit-user',
  templateUrl: './edit-user.component.html',
  styleUrl: './edit-user.component.css',
})
export class EditUserComponent {
  novoUsuario: any = {};
  nome: string = '';
  email: string = '';
  reputacao: number = 0;

  constructor(
    private usuarioService: UsuarioService,
    private router: Router,
    private actvRoute: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.actvRoute.params.subscribe((params) => {
      this.novoUsuario = {
        id: params['id_user'],
        nome: params['nome'],
        email: params['email'],
        reputacao: params['reputacao'] || 0,
      };
    });

    this.nome = this.novoUsuario.nome;
    this.email = this.novoUsuario.email;
    this.reputacao = this.novoUsuario.reputacao;
  }

  salvarUsuario() {
    this.novoUsuario.nome = this.nome;
    this.novoUsuario.email = this.email;
    this.novoUsuario.reputacao = this.reputacao;

    this.usuarioService
      .editUsuario(this.novoUsuario.id, this.novoUsuario)
      .subscribe(() => {
        this.router.navigate(['/usuarios']);
      });
  }
}

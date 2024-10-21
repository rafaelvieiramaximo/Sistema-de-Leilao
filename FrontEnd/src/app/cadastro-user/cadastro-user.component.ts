import { Component } from '@angular/core';
import { UsuarioService } from '../services/usuario.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cadastro-user',
  templateUrl: './cadastro-user.component.html',
  styleUrls: ['./cadastro-user.component.css']
})
export class CadastroUserComponent {
  nome: string = '';
  email: string = '';
  senha: string = '';
  confirmarSenha: string = '';

  constructor(private usuarioService: UsuarioService, private router: Router) {}

  cadastrarUsuario() {
    if (this.senha !== this.confirmarSenha) {
      alert('As senhas não conferem!');
      return;
    }

    const novoUsuario = {
      nome: this.nome,
      email: this.email,
      senha: this.senha,
      reputacao: 0 // Defina um valor padrão ou deixe para a API calcular
    };

    this.usuarioService.createUsuario(novoUsuario).subscribe(
      response => {
        alert('Usuário cadastrado com sucesso!');
        this.router.navigate(['/usuarios']); // Navegar para a página de usuários cadastrados
      },
      error => {
        console.error('Erro ao cadastrar usuário:', error);
        alert('Erro ao cadastrar usuário. Tente novamente.');
      }
    );
  }
}

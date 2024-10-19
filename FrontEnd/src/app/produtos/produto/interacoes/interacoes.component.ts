import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';
import { Produto } from '../../../services/produto.service';

@Component({
  selector: 'app-interacoes',
  templateUrl: './interacoes.component.html',
  styleUrls: ['./interacoes.component.css'],
})
export class InteracoesComponent {
  @Input() produto!: Produto;

  constructor(private router: Router) {}

  navAvaliacao() {
    this.router.navigate(['/avaliacoes', this.produto.id_produto]);
  }

  navLances() {
    this.router.navigate(['/lances', this.produto.id_produto]);
  }
}

import { Component, Input, OnInit } from '@angular/core';
import { Produto } from '../../services/produto.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-produto',
  templateUrl: './produto.component.html',
  styleUrls: ['./produto.component.css'],
})
export class ProdutoComponent {
  @Input() produto!: Produto;

  constructor(private router: Router) {}

  navAvaliacao() {
    this.router.navigate(['/avaliacoes', this.produto.id_produto]);
  }

  navLances() {
    // this.router.navigate(['/lances', this.produto.id_produto]);
    console.log(this.produto);
  }
}

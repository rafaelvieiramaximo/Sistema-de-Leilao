import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-produtos',
  templateUrl: './produtos.component.html',
  styleUrl: './produtos.component.css',
})
export class ProdutosComponent {
  constructor(private router: Router) {}

  navAnunciarProduto() {
    this.router.navigate(['/cadastro-produtos']);
  }
}

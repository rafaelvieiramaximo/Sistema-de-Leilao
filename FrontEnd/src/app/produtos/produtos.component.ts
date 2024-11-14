import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'; // Importando o Router
import { ProdutoService, Produto } from '../services/produto.service'; // Certifique-se que o caminho do serviço está correto

@Component({
  selector: 'app-produtos',
  templateUrl: './produtos.component.html',
  styleUrls: ['./produtos.component.css'],
})
export class ProdutosComponent implements OnInit {


  produtos: Produto[] = []; // Declaração da propriedade 'produtos'

  // Injetando o Router no construtor
  constructor(private produtoService: ProdutoService, private router: Router) {}

  // Carrega a lista de produtos ao iniciar o componente
  ngOnInit(): void {
    this.produtoService.getProdutos().subscribe((data: Produto[]) => {
      this.produtos = data;
    });
  }

  // Navega para o cadastro de produtos
  navAnunciarProduto() {
    this.router.navigate(['/cadastro-produtos']);
  }
}

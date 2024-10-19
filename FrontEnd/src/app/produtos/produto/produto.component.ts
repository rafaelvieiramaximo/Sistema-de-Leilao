import { Component, Input, OnInit } from '@angular/core';
import { Produto } from '../../services/produto.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-produto',
  templateUrl: './produto.component.html',
  styleUrls: ['./produto.component.css'],
})
export class ProdutoComponent implements OnInit {
  @Input() produto!: Produto;

  constructor(private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.produto = {
        id_produto: +params['id_produto'] || this.produto.id_produto,
        nome: params['nome'] || this.produto.nome,
        descricao: params['descricao'] || this.produto.descricao,
        preco_inicial: +params['preco'] || this.produto.preco_inicial,
        data_inicial: params['data'] || this.produto.data_inicial,
      };
    });
  }

  navAvaliacao(produtoLink: Produto) {
    this.router.navigate([
      '/avaliacoes',
      produtoLink.data_inicial,
      produtoLink.descricao,
      produtoLink.id_produto,
      produtoLink.nome,
      produtoLink.preco_inicial,
    ]);
  }

  navLances(produtoLink: Produto) {
    this.router.navigate([
      '/lances',
      produtoLink.data_inicial,
      produtoLink.descricao,
      produtoLink.id_produto,
      produtoLink.nome,
      produtoLink.preco_inicial,
    ]);
  }
}

import { Component } from '@angular/core';
import { Avaliacao, AvaliacaoService } from '../services/avaliacao.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-avaliacoes',
  templateUrl: './avaliacoes.component.html',
  styleUrl: './avaliacoes.component.css',
})
export class AvaliacoesComponent {
  lancesProduto: Avaliacao[] = [];

  constructor(
    private avaliacaoServ: AvaliacaoService,
    private actvRoute: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.actvRoute.params.subscribe((params) => {
      const produtoId = params['id_produto'];

      this.avaliacaoServ.getAvaliacoesByProdutoId(produtoId).subscribe({
        next: (avaliacoes: Avaliacao[]) => {
          this.lancesProduto = avaliacoes;
        },
        error: (err) => {
          console.error('Erro ao buscar avaliações:', err);
        },
      });
    });
  }
}

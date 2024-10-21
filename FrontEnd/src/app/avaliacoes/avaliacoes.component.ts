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
  id_user: number | null = null;
  texto: string = '';

  dataAtual = new Date();
  dia = String(this.dataAtual.getDate()).padStart(2, '0');
  mes = String(this.dataAtual.getMonth() + 1).padStart(2, '0');
  ano = this.dataAtual.getFullYear();
  dataFormatada = `${this.ano}-${this.mes}-${this.dia}`;
  produtoId: number = 0;

  constructor(
    private avaliacaoServ: AvaliacaoService,
    private actvRoute: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.actvRoute.params.subscribe((params) => {
      this.produtoId = params['id_produto'];

      this.avaliacaoServ.getAvaliacoesByProdutoId(this.produtoId).subscribe({
        next: (avaliacoes: Avaliacao[]) => {
          this.lancesProduto = avaliacoes;
        },
        error: (err) => {
          console.error('Erro ao buscar avaliações:', err);
        },
      });
    });
  }

  cadastroAval() {
    const novaAval = {
      id_usuario: this.id_user !== null ? this.id_user : 0,
      texto: this.texto,
      data: this.dataFormatada,
      id_produto: +this.produtoId,
    };

    this.avaliacaoServ.createAvaliacao(novaAval).subscribe({
      next: (avaliacaoCriada) => {
        console.log('Avaliação criada com sucesso:', avaliacaoCriada);
        // Você pode adicionar lógica para atualizar a interface ou navegar
      },
      error: (err) => {
        console.error('Erro ao criar avaliação:', err);
      },
    });
  }
}

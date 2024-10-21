import { Component } from '@angular/core';
import { Lance, LanceService } from '../services/lance.service';
import { AvaliacaoService } from '../services/avaliacao.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-lances',
  templateUrl: './lances.component.html',
  styleUrl: './lances.component.css',
})
export class LancesComponent {
  lancesProduto: Lance[] = [];
  id_user: number | null = null;
  valor: number = 0;

  dataAtual = new Date();
  dia = String(this.dataAtual.getDate()).padStart(2, '0');
  mes = String(this.dataAtual.getMonth() + 1).padStart(2, '0');
  ano = this.dataAtual.getFullYear();
  dataFormatada = `${this.ano}-${this.mes}-${this.dia}`;
  produtoId: number = 0;

  constructor(
    private lanceSrv: LanceService,
    private actvRoute: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.actvRoute.params.subscribe((params) => {
      this.produtoId = params['id_produto'];

      this.lanceSrv.getLancesByProdutoId(this.produtoId).subscribe({
        next: (lances: Lance[]) => {
          this.lancesProduto = lances;
        },
        error: (err) => {
          console.error('Erro ao buscar avaliações:', err);
        },
      });
    });
  }

  cadastroAval() {
    const novoLance = {
      id_usuario: this.id_user !== null ? this.id_user : 0,
      valor: this.valor,
      data: this.dataFormatada,
      id_produto: +this.produtoId,
    };

    this.lanceSrv.createLance(novoLance).subscribe({
      next: (lanceCriado) => {
        console.log('Lance criado com sucesso:', lanceCriado);
      },
      error: (err) => {
        console.error('Erro ao criar avaliação:', err);
      },
    });
  }
}

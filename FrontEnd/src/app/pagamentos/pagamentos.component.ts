import { Component } from '@angular/core';
import { PagamentoService } from '../services/pagamento.service';

@Component({
  selector: 'app-pagamentos',
  templateUrl: './pagamentos.component.html',
  styleUrl: './pagamentos.component.css'
})
export class PagamentosComponent {

  pagamentos: any [] = [];
  
  constructor(private pagamentoService: PagamentoService){ }

  //Inicia o com o GET
  ngOnInit(): void {
    this.pagamentoService.getPagamentos().subscribe(data => {
      this.pagamentos = data;
    });
  }

  


}

import { Component, OnInit } from '@angular/core';
import { PagamentoService } from '../services/pagamento.service';

@Component({
  selector: 'app-pagamentos',
  templateUrl: './pagamentos.component.html',
  styleUrls: ['./pagamentos.component.css']
})
export class PagamentosComponent implements OnInit {
  pagamentos: any[] = [];
  displayStyle = "none";

  constructor(private pagamentoService: PagamentoService) { }

  ngOnInit(): void {
    this.pagamentoService.getPagamentos().subscribe(data => {
      this.pagamentos = data;
    });
  }

  openModal() {
    this.displayStyle = "block";
  }

  closeModal() {
    this.displayStyle = "none";
  }

  addPagamento(event: Event) {
    const form = event.target as HTMLFormElement;
    
    const novoPagamento = {
      id_usuario: form['id_usuario'].value,
      id_produto: form['id_produto'].value,
      valor_total: form['valor_total'].value,
      forma_pagamento: form['forma_pagamento'].value,
      status: form['status'].value
    };

    this.pagamentoService.addPagamento(novoPagamento).subscribe((response: any) => {
      this.pagamentos.push(response);
      this.closeModal();
    });

  }
}

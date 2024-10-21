import { Component, Input, OnInit } from '@angular/core';
import { Avaliacao } from '../../services/avaliacao.service';

@Component({
  selector: 'app-avaliacao',
  templateUrl: './avaliacao.component.html',
  styleUrl: './avaliacao.component.css',
})
export class AvaliacaoComponent implements OnInit {
  @Input() avaliacao!: Avaliacao;

  id: number = 0;
  texto: string = '';
  data: string = '';
  id_usuario: number = 0;
  id_produto: number = 0;

  ngOnInit(): void {
    this.id_usuario = this.avaliacao.id_usuario;
    this.id_produto = this.avaliacao.id_produto;
    this.texto = this.avaliacao.texto;
    this.data = this.avaliacao.data;
  }
}

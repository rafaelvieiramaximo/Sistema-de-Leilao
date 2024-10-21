import { Component, Input } from '@angular/core';
import { Lance } from '../../services/lance.service';

@Component({
  selector: 'app-lance',
  templateUrl: './lance.component.html',
  styleUrl: './lance.component.css',
})
export class LanceComponent {
  @Input() lance!: Lance;

  id: number = 0;
  valor_lance: number = 0;
  data: string = '';
  id_usuario: number = 0;
  id_produto: number = 0;

  ngOnInit(): void {
    this.id_usuario = this.lance.id_usuario;
    this.id_produto = this.lance.id_produto;
    this.valor_lance = this.lance.valor_lance;
    this.data = this.lance.data;
  }
}

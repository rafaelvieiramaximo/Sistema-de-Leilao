import { Component, Input } from '@angular/core';
import { Comunidade, ComunidadeService } from '../../services/comunidade.service';
import { Usuario } from '../../services/usuario.service';

@Component({
  selector: 'app-comunidade',
  templateUrl: './comunidade.component.html',
  styleUrl: './comunidade.component.css'
})
export class ComunidadeComponent {
  @Input() comunidade!: Comunidade;
  @Input() usuario!: Usuario;

   constructor( private comunidadeService: ComunidadeService) {}

}

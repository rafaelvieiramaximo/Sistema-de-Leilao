import { Component } from '@angular/core';
import { Comunidade, ComunidadeService } from '../services/comunidade.service';

@Component({
  selector: 'app-comunidades',
  templateUrl: './comunidades.component.html',
  styleUrl: './comunidades.component.css'
})
export class ComunidadesComponent {
    comunidades: Comunidade[] = [];

    constructor( private comunidadeService: ComunidadeService) { }

    ngOnInit(): void {
      this.comunidadeService.getComunidades().subscribe((data: Comunidade[]) => {
        this.comunidades = data; 
      });
  }
}
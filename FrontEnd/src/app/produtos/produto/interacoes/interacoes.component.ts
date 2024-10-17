import { Component } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';

@Component({
  selector: 'app-interacoes',
  templateUrl: './interacoes.component.html',
  styleUrl: './interacoes.component.css',
})
export class InteracoesComponent {
  constructor(private router: Router, private route: ActivatedRoute) {}

  produto: { id: number } = { id: 0 };

  navAvaliacao() {
    this.router.navigate(['/avaliacoes', this.produto.id]);

    this.route.params.subscribe((params: Params) => {
      this.produto.id = params['id'];
    });
  }
}

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CadastroUserComponent } from './cadastro-user/cadastro-user.component';
import { ProdutosComponent } from './produtos/produtos.component';
import { CadastroProdutosComponent } from './cadastro-produtos/cadastro-produtos.component';
import { LancesComponent } from './lances/lances.component';
import { AvaliacoesComponent } from './avaliacoes/avaliacoes.component';
import { UsuariosComponent } from './usuarios/usuarios.component';

const routes: Routes = [
  { path: '', component: CadastroUserComponent },
  { path: 'produtos', component: ProdutosComponent },
  { path: 'cadastro-produtos', component: CadastroProdutosComponent },
  { path: 'lances/:id', component: LancesComponent },
  { path: 'avaliacoes/:id', component: AvaliacoesComponent },
  { path: 'usuarios', component: UsuariosComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}

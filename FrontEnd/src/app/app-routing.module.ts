import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { CadastroUserComponent } from './cadastro-user/cadastro-user.component';
import { ProdutosComponent } from './produtos/produtos.component';
import { CadastroProdutosComponent } from './cadastro-produtos/cadastro-produtos.component';
import { LancesComponent } from './lances/lances.component';
import { AvaliacoesComponent } from './avaliacoes/avaliacoes.component';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'cadastro-user', component: CadastroUserComponent },
  { path: 'produtos', component: ProdutosComponent },
  { path: 'cadastro-produtos', component: CadastroProdutosComponent },
  { path: 'lances', component: LancesComponent },
  { path: 'avaliacoes', component: AvaliacoesComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CadastroUserComponent } from './cadastro-user/cadastro-user.component';
import { ProdutosComponent } from './produtos/produtos.component';
import { CadastroProdutosComponent } from './cadastro-produtos/cadastro-produtos.component';
import { LancesComponent } from './lances/lances.component';
import { AvaliacoesComponent } from './avaliacoes/avaliacoes.component';
import { UsuariosComponent } from './usuarios/usuarios.component';
import { PagamentosComponent } from './pagamentos/pagamentos.component';

const routes: Routes = [
  { path: 'usuario', component: CadastroUserComponent },
  { path: 'produtos', component: ProdutosComponent },
  { path: 'cadastro-produtos', component: CadastroProdutosComponent },
  {
    path: 'lances/:data/:descricao/:id_produto/:nome/:preco',
    component: LancesComponent,
  },
  {
    path: 'avaliacoes/:data/:descricao/:id_produto/:nome/:preco',
    component: AvaliacoesComponent,
  },
  { path: 'usuarios', component: UsuariosComponent },
  {path: 'pagamentos', component: PagamentosComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}

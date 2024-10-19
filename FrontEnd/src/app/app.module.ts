import { NgModule } from '@angular/core';
import {
  BrowserModule,
  provideClientHydration,
} from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainCardComponent } from './main-card/main-card.component';
import { ProdutosComponent } from './produtos/produtos.component';
import { ProdutoComponent } from './produtos/produto/produto.component';
import { CadastroUserComponent } from './cadastro-user/cadastro-user.component';
import { CadastroProdutosComponent } from './cadastro-produtos/cadastro-produtos.component';
import { LancesComponent } from './lances/lances.component';
import { AvaliacoesComponent } from './avaliacoes/avaliacoes.component';
import { InteracoesComponent } from './produtos/produto/interacoes/interacoes.component';
import { AvaliacaoComponent } from './avaliacoes/avaliacao/avaliacao.component';
import { LanceComponent } from './lances/lance/lance.component';
import { HttpClientModule } from '@angular/common/http';
import { UsuariosComponent } from './usuarios/usuarios.component';
import { UsuarioComponent } from './usuarios/usuario/usuario.component';

@NgModule({
  declarations: [
    AppComponent,
    MainCardComponent,
    ProdutosComponent,
    ProdutoComponent,
    CadastroUserComponent,
    CadastroProdutosComponent,
    LancesComponent,
    AvaliacoesComponent,
    InteracoesComponent,
    AvaliacaoComponent,
    LanceComponent,
    UsuariosComponent,
    UsuarioComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, HttpClientModule],
  providers: [provideClientHydration()],
  bootstrap: [AppComponent],
})
export class AppModule {}

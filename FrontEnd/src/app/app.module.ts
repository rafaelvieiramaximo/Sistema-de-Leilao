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
import { LoginComponent } from './login/login.component';
import { CadastroUserComponent } from './cadastro-user/cadastro-user.component';
import { CadastroProdutosComponent } from './cadastro-produtos/cadastro-produtos.component';
import { LancesComponent } from './lances/lances.component';
import { AvaliacoesComponent } from './avaliacoes/avaliacoes.component';
import { InteracoesComponent } from './produtos/produto/interacoes/interacoes.component';

@NgModule({
  declarations: [AppComponent, MainCardComponent, ProdutosComponent, ProdutoComponent, LoginComponent, CadastroUserComponent, CadastroProdutosComponent, LancesComponent, AvaliacoesComponent, InteracoesComponent],
  imports: [BrowserModule, AppRoutingModule],
  providers: [provideClientHydration()],
  bootstrap: [AppComponent],
})
export class AppModule {}

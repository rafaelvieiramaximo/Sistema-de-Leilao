import { Component } from '@angular/core';
import { Produto, ProdutoService } from '../services/produto.service'; // Ajuste o caminho conforme necessário
import { Router } from '@angular/router'; // Importando Router para redirecionamento

@Component({
  selector: 'app-cadastro-produtos',
  templateUrl: './cadastro-produtos.component.html', // O template HTML para este componente
  styleUrls: ['./cadastro-produtos.component.css'] // Estilos opcionais
})
export class CadastroProdutosComponent {
  produto: Partial<Produto> = {
    nome: '',
    descricao: '',
    preco_inicial: 0,
    data_inicial: '',
    id_usuario: 1 // Altere conforme a lógica do seu app
  };

  constructor(private produtoService: ProdutoService, private router: Router) { }

  cadastrarProduto() {
    this.produtoService.createProduto(this.produto).subscribe({
      next: (response) => {
        console.log('Produto cadastrado com sucesso:', response);
        // Redirecionar ou exibir mensagem de sucesso
        this.router.navigate(['/produtos']); // Redireciona para a lista de produtos ou outra rota desejada
      },
      error: (error) => {
        console.error('Erro ao cadastrar produto:', error);
        // Adicione lógica para manipular o erro, como exibir uma mensagem ao usuário
      }
    });
  }
}

# Sistema de Leilão Online - Documentação

Este projeto é uma API backend desenvolvida em **Flask** para um sistema de leilão online. Ele inclui diversas funcionalidades, como cadastro de usuários, produtos, lances, pagamentos, fretes, avaliações e comunidades, utilizando um banco de dados PostgreSQL.

## Sumário
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Modelos de Dados](#modelos-de-dados)
  - [Usuários](#usuários)
  - [Produtos](#produtos)
  - [Lances](#lances)
  - [Pagamentos](#pagamentos)
  - [Frete](#frete)
  - [Avaliações](#avaliações)
  - [Comunidades](#comunidades)
- [Rotas da API](#rotas-da-api)
- [Triggers](#triggers)
- [Variáveis de Ambiente](#variáveis-de-ambiente)
- [Autores](#autores)

---

## Instalação

1. **Clone o repositório:**
   ```bash
     git clone https://github.com/seuusuario/sistema-de-leilao.git
     cd sistema-de-leilao
2. **Crie um ambiente virtual:
   
    ```bash
    Copie o código abaixo
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    Instale as dependências:

    ```bash
    Copiar código
    pip install -r requirements.txt
    Configure o banco de dados: Certifique-se de que você tem uma instância do PostgreSQL rodando. Crie um banco de dados e adicione a URL de conexão no arquivo .env:
    
    plaintext
    Copiar código
    DB_KEY=postgresql://usuario:senha@localhost:5432/nome_do_banco
    Inicie o servidor:
    
    bash
    Copiar código
    flask run

**Estrutura do BackEnd
├── app/
│   ├── __init__.py          # Configurações do Flask e SQLAlchemy
│   ├── routes.py            # Definição das rotas da API
│   ├── models/
│   │   ├── usuario.py       # Modelo de Usuário
│   │   ├── produto.py       # Modelo de Produto
│   │   ├── lance.py         # Modelo de Lance
│   │   ├── pagamento.py     # Modelo de Pagamento
│   │   ├── frete.py         # Modelo de Frete
│   │   ├── avaliacao.py     # Modelo de Avaliação
│   │   └── comunidade.py    # Modelo de Comunidade
├── .env                     # Variáveis de ambiente
├── requirements.txt         # Dependências do projeto
├── run.py                   # Ponto de entrada do Flask
└── README.md                # Documentação do projeto


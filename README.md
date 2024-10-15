Aqui está a documentação que você pode anexar ao seu repositório no GitHub para o projeto de leilão online desenvolvido em **Flask**.

---

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
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados:**
   Certifique-se de que você tem uma instância do PostgreSQL rodando. Crie um banco de dados e adicione a URL de conexão no arquivo `.env`:
   ```plaintext
   DB_KEY=postgresql://usuario:senha@localhost:5432/nome_do_banco
   ```

5. **Inicie o servidor:**
   ```bash
   flask run
   ```

---

## Estrutura do Projeto

```bash
.
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
```

---

## Modelos de Dados

### Usuários

Representa os usuários registrados no sistema.

```python
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    reputacao = db.Column(db.Float, default=0)
```

### Produtos

Representa os produtos que estão sendo leiloados.

```python
class Produto(db.Model):
    __tablename__ = 'produtos'
    id_produto = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    preco_inicial = db.Column(db.Float, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
```

### Lances

Registra os lances feitos nos produtos.

```python
class Lance(db.Model):
    __tablename__ = 'lances'
    id_lance = db.Column(db.Integer, primary_key=True)
    valor_lance = db.Column(db.Float, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produtos.id_produto'), nullable=False)
```

### Pagamentos

Armazena os detalhes de pagamento dos produtos vendidos【64†source】.

```python
class Pagamento(db.Model):
    __tablename__ = 'pagamentos'
    id_pagamento = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produtos.id_produto'), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    forma_pagamento = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
```

### Frete

Registra as informações de frete associadas ao pagamento【63†source】.

```python
class Frete(db.Model):
    __tablename__ = 'frete'
    cte = db.Column(db.Integer, primary_key=True)
    tipo_frete = db.Column(db.String(255), nullable=False)
    valor_frete = db.Column(db.Float)
    prazo_entrega = db.Column(db.Integer)
    id_pagamento = db.Column(db.Integer, db.ForeignKey('pagamentos.id_pagamento'))
```

### Avaliações

Permite que os usuários avaliem os produtos【61†source】.

```python
class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'
    id_avaliacao = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    data = db.Column(db.Date, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produtos.id_produto'), nullable=False)
```

### Comunidades

Representa as comunidades de usuários dentro do sistema【62†source】.

```python
class Comunidade(db.Model):
    __tablename__ = 'comunidade'
    id_comunidade = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
```

---

## Rotas da API

### Usuários
- **GET /usuarios**: Lista todos os usuários.
- **POST /usuarios**: Cria um novo usuário.

### Produtos
- **GET /produtos**: Lista todos os produtos.
- **POST /produtos**: Adiciona um novo produto.

### Lances
- **GET /lances**: Lista todos os lances.
- **POST /lances**: Adiciona um novo lance.

### Pagamentos
- **GET /pagamentos**: Lista todos os pagamentos.
- **POST /pagamentos**: Adiciona um novo pagamento.

### Fretes
- **GET /fretes**: Lista todas as informações de frete.
- **POST /fretes**: Adiciona uma nova informação de frete.

### Avaliações
- **GET /avaliacoes**: Lista todas as avaliações.
- **POST /avaliacoes**: Adiciona uma nova avaliação.

### Comunidades
- **GET /comunidades**: Lista todas as comunidades.
- **POST /comunidades**: Cria uma nova comunidade.

---

## Triggers

### Trigger para Evitar Produtos Duplicados

No banco de dados, foi configurado um **trigger** que impede a inserção de produtos com nomes duplicados.

**Função do Trigger**:
```sql
CREATE OR REPLACE FUNCTION verificar_produto_nome_duplicado()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM produtos WHERE nome = NEW.nome) THEN
        RAISE EXCEPTION 'Produto com o nome "%" já existe.', NEW.nome;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

**Trigger**:
```sql
CREATE TRIGGER trigger_produto_nome_duplicado
BEFORE INSERT ON produtos
FOR EACH ROW
EXECUTE FUNCTION verificar_produto_nome_duplicado();
```

---

## Variáveis de Ambiente

Você precisa definir as seguintes variáveis no arquivo `.env`:

```plaintext
DB_KEY=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

---

## Autores

- **Seu Nome** - Desenvolvedor
- **Contribuidores** - Lista de contribuidores

---

Essa documentação cobre o uso da aplicação, os modelos de dados e as rotas da API para o sistema de leilão online desenvolvido com Flask.

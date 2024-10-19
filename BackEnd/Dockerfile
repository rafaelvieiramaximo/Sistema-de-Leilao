# Usar imagem Python slim
FROM python:3.9-slim

# Expor a porta 5000
EXPOSE 5000

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Atualizar o pip
RUN pip install --upgrade pip

# Instalar as dependências necessárias para compilar psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Instalar as dependências Python
RUN pip install -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta 5000 novamente (não é necessário, você já fez isso antes)
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "run.py"]

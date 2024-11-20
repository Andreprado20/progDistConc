#!/bin/bash

# Nome do diretório do projeto
PROJECT_NAME="cryptowallet"

# Criar a estrutura de diretórios
mkdir -p $PROJECT_NAME/routes

# Criar os arquivos principais
touch $PROJECT_NAME/app.py
touch $PROJECT_NAME/config.py
touch $PROJECT_NAME/models.py
touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/.env

# Criar arquivos dentro do diretório routes
touch $PROJECT_NAME/routes/carteira_routes.py
touch $PROJECT_NAME/routes/cripto_routes.py
touch $PROJECT_NAME/routes/transacao_routes.py

# Exibir a estrutura criada
echo "Estrutura do projeto criada:"
tree $PROJECT_NAME

# Mensagem final
echo "Projeto '$PROJECT_NAME' configurado com sucesso!"

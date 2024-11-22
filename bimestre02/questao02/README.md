# API de Horóscopo / Horoscope API

[English version below](#english-version)

## Português

### Sobre o Projeto
Este é um sistema de API de horóscopo que oferece previsões astrológicas com dois níveis de acesso: básico e avançado. O projeto é composto por um servidor Flask (Python) e um cliente TypeScript, implementando um sistema simples de autenticação e diferentes níveis de acesso às previsões.

### Funcionalidades
- Criação de usuários com diferentes planos (básico/avançado)
- Sistema de login
- Consulta de horóscopo personalizada
- Planos diferenciados (básico: apenas mensagem / avançado: mensagem + número da sorte)

### Pré-requisitos
- Python 3.6+
- Node.js 12+
- npm ou yarn

### Instalação

1. Clone o repositório
```bash
git clone [url-do-repositorio]
```

2. Instale as dependências do servidor (Python)
```bash
cd server
pip install flask
```

3. Instale as dependências do cliente (TypeScript)
```bash
cd client
npm install
# ou
yarn install
```

### Como Executar

1. Inicie o servidor Flask
```bash
cd server
python app.py
```

2. Em outro terminal, execute o cliente
```bash
cd client
ts-node client.ts
```

### Estrutura da API

#### Endpoints

1. POST /create_user
   - Cria um novo usuário
   - Parâmetros: nickname, plan (basic/advanced)

2. POST /login
   - Autentica um usuário
   - Parâmetros: nickname

3. POST /horoscope
   - Retorna o horóscopo do dia
   - Parâmetros: nickname, sign

### Exemplos de Uso
O cliente TypeScript inclui exemplos de como:
- Criar um novo usuário
- Fazer login
- Consultar o horóscopo

---

## English Version

### About the Project
This is a horoscope API system that provides astrological predictions with two access levels: basic and advanced. The project consists of a Flask server (Python) and a TypeScript client, implementing a simple authentication system and different levels of access to predictions.

### Features
- User creation with different plans (basic/advanced)
- Login system
- Customized horoscope consultation
- Different plans (basic: message only / advanced: message + lucky number)

### Prerequisites
- Python 3.6+
- Node.js 12+
- npm or yarn

### Installation

1. Clone the repository
```bash
git clone [repository-url]
```

2. Install server dependencies (Python)
```bash
cd server
pip install flask
```

3. Install client dependencies (TypeScript)
```bash
cd client
npm install
# or
yarn install
```

### How to Run

1. Start the Flask server
```bash
cd server
python app.py
```

2. In another terminal, run the client
```bash
cd client
ts-node client.ts
```

### API Structure

#### Endpoints

1. POST /create_user
   - Creates a new user
   - Parameters: nickname, plan (basic/advanced)

2. POST /login
   - Authenticates a user
   - Parameters: nickname

3. POST /horoscope
   - Returns the daily horoscope
   - Parameters: nickname, sign

### Usage Examples
The TypeScript client includes examples of how to:
- Create a new user
- Login
- Check the horoscope
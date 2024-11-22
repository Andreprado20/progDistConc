# Conversor de Moedas / Currency Converter

[English Version](#english-version)

## Versão em Português

### Sobre o Projeto
Este é um aplicativo web desenvolvido com Next.js que exibe as taxas de câmbio em tempo real para diferentes moedas (Real Brasileiro, Euro e Iene Japonês) em relação ao Dólar Americano. O projeto utiliza a API ExchangeRate para obter dados atualizados das cotações.

### Funcionalidades
- Exibição em tempo real das taxas de câmbio
- Interface moderna com efeitos de gradiente
- Links para mais cotações e informações sobre a API
- Design responsivo e intuitivo

### Pré-requisitos
- Node.js (versão 14 ou superior)
- npm ou yarn
- Conta na ExchangeRate API (para obter a chave de API)

### Instalação

1. Clone o repositório
```bash
git clone [url-do-repositorio]
```

2. Instale as dependências
```bash
npm install
# ou
yarn install
```

3. Configure as variáveis de ambiente
Crie um arquivo `.env.local` na raiz do projeto e adicione sua chave da API:
```
NEXT_PUBLIC_EXCHANGE_RATE_API_KEY=sua_chave_aqui
```

4. Inicie o servidor de desenvolvimento
```bash
npm run dev
# ou
yarn dev
```

### Tecnologias Utilizadas
- Next.js 13+
- React
- Tailwind CSS
- shadcn/ui
- ExchangeRate API

### Estrutura do Projeto
- `page.tsx`: Componente principal que exibe as cotações
- `components/ui`: Componentes reutilizáveis do shadcn/ui
- Utiliza o App Router do Next.js
- Implementa Server Components e Client Components

OBS: Este projeto já tem um deploy público feito na plataforma Vercel e está disponível através do seguinte [link](https://questao01-fetch-currencies.vercel.app/)

---

## English Version

### About the Project
This is a web application developed with Next.js that displays real-time exchange rates for different currencies (Brazilian Real, Euro, and Japanese Yen) against the US Dollar. The project uses the ExchangeRate API to obtain updated exchange rate data.

### Features
- Real-time display of exchange rates
- Modern interface with gradient effects
- Links to more exchange rates and API information
- Responsive and intuitive design

### Prerequisites
- Node.js (version 14 or higher)
- npm or yarn
- ExchangeRate API account (to obtain API key)

### Installation

1. Clone the repository
```bash
git clone [repository-url]
```

2. Install dependencies
```bash
npm install
# or
yarn install
```

3. Configure environment variables
Create a `.env.local` file in the project root and add your API key:
```
NEXT_PUBLIC_EXCHANGE_RATE_API_KEY=your_key_here
```

4. Start the development server
```bash
npm run dev
# or
yarn dev
```

### Technologies Used
- Next.js 13+
- React
- Tailwind CSS
- shadcn/ui
- ExchangeRate API

### Project Structure
- `page.tsx`: Main component that displays exchange rates
- `components/ui`: Reusable shadcn/ui components
- Uses Next.js App Router
- Implements Server Components and Client Components

OBS: This page is currently publicly available on the Vercel platform by the following [URL link](https://questao01-fetch-currencies.vercel.app/)
# 🏦 Sistema Bancário em Python com Interface Gráfica
## AINDA EM DESENVOVIMENTO ##


Este projeto é um sistema bancário simples desenvolvido em Python, que utiliza arquivos JSON para persistência de dados e Tkinter para a interface gráfica. O sistema permite cadastrar clientes, criar contas, realizar depósitos, saques, consultar extratos e buscar clientes.

---

## 🚀 Tecnologias

- Python 3.x

## 📂 Estrutura do Projeto

### 1. `clientes.py` 👥

- Gerencia o cadastro e armazenamento dos clientes.
- Cada cliente possui:
  - 🧑 Nome
  - 🎂 Data de nascimento
  - 🆔 CPF (único)
  - 🏠 Endereço
- Os dados são salvos em arquivo JSON (`clientes.json`) para persistência.
- Possui funções para cadastrar clientes e buscar cliente por CPF.

### 2. `contas.py` 💳

- Gerencia as contas bancárias associadas aos clientes.
- Cada conta possui:
  - 🔢 Número da conta (único e sequencial)
  - 🆔 CPF do cliente titular
  - 💰 Saldo
  - 📄 Extrato de transações (depósitos e saques)
  - 🚫 Limite de saques diários
- As contas são salvas em arquivo JSON (`contas.json`).
- Permite criar contas, buscar contas por número e listar todas as contas.

### 3. `transacoes.py` 🔄 (se existir)
<<<<<<< HEAD

- Implementa operações financeiras como depósito e saque.
- Controla regras como limite diário de saques e validação de saldo.
- Atualiza o extrato das contas com cada transação realizada.

### 4. `main.py` 🖥️

- Interface de linha de comando (CLI) para interagir com o sistema.
- Oferece menu com opções para cadastro, criação de conta, depósito, saque, extrato e busca de clientes.

### 5. `interface.py` 🎨

- Interface gráfica desenvolvida com Tkinter.
- Janela principal com botões para acessar funcionalidades:
  - 👤 Cadastrar cliente
  - 🏦 Criar conta
  - 🔐 Selecionar conta
  - 🚪 Sair
- Tela de cadastro de cliente com formulário para entrada de dados.
- Integração com os módulos de backend para persistência e lógica de negócio.


## AINDA EM DESENVOVIMENTO ##
=======

- Implementa operações financeiras como depósito e saque.
- Controla regras como limite diário de saques e validação de saldo.
- Atualiza o extrato das contas com cada transação realizada.

### 4. `main.py` 🖥️

- Interface de linha de comando (CLI) para interagir com o sistema.
- Oferece menu com opções para cadastro, criação de conta, depósito, saque, extrato e busca de clientes.

### 5. `interface.py` 🎨

- Interface gráfica desenvolvida com Tkinter.
- Janela principal com botões para acessar funcionalidades:
  - 👤 Cadastrar cliente
  - 🏦 Criar conta
  - 🔐 Selecionar conta
  - 🚪 Sair
- Tela de cadastro de cliente com formulário para entrada de dados.
- Integração com os módulos de backend para persistência e lógica de negócio.





# Cadastro - Sistema Bancário

Este projeto é parte dos desafios do curso de Python.

## 📋 Descrição

Sistema simples de cadastro bancário com funcionalidades como:
- Cadastro de clientes
- Criação de contas
- Operações básicas (depósito, saque, extrato)
- Validações de CPF e limite de saques

## 🚀 Tecnologias

- Python 3.x

## 🧠 Aprendizados

- Manipulação de dados com dicionários
- Organização de código em funções
- Boas práticas com PEP8
- Tipos de passagem de argumentos em funções (`positional-only`, `keyword-only`)

## ⚙️ Funcionalidades e Regras

### 📥 Depósito
- Deve receber **apenas argumentos posicionais**.
- Argumentos esperados: `saldo`, `valor`, `extrato`.
- Retorna: novo `saldo` e `extrato`.

### 💸 Saque
- Deve receber **apenas argumentos nomeados** (`keyword only`).
- Argumentos esperados: `saldo`, `valor`, `extrato`, `limite_saques`.
- Retorna: novo `saldo` e `extrato`.

### 📄 Extrato
- Deve receber os argumentos **por posição e por nome**.
- Utiliza: `positional-only` e `keyword-only` corretamente.

### 👤 Cadastro de Clientes
- Campos obrigatórios:
  - Nome
  - Data de nascimento
  - CPF (**apenas um CPF por cliente**)
  - Endereço

### 🔍 Busca de Cliente
- Busca realizada com base no CPF informado.

## 📂 Estrutura


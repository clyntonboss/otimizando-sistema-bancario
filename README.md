# 💳 Sistema Bancário em Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![DIO](https://img.shields.io/badge/DIO-Digital%20Innovation%20One-orange)
![Curso](https://img.shields.io/badge/Curso-Back-End%20com%20Python-green)

## 🏷️ Projeto

Este projeto faz parte do curso **Back-End com Python™** da **Digital Innovation One (DIO)**, no módulo **Dominando Funções e Boas Práticas em Python™**, subcurso **Otimizando o Sistema Bancário com Funções Python™**.

O objetivo é **modularizar o código, aplicar boas práticas de programação e trabalhar com funções em Python**, simulando um **sistema bancário completo**.

---

## 📝 Funcionalidades

### 👤 Cadastro de Usuário (Cliente)
- Solicita: nome, data de nascimento, CPF e endereço.
- Valida CPF e impede duplicidade.
- Formata CPF (XXX.XXX.XXX-XX) e CEP (XXXXX-XXX) automaticamente.
- Armazena dados em uma lista de usuários.

### 🏦 Criação de Conta
- Vincula conta a usuário existente via CPF.
- Cada conta possui:
  - Agência: `0001`
  - Número de conta sequencial
  - Saldo inicial `0`
  - Extrato vazio
  - Contador de saques
- Um usuário pode ter várias contas; uma conta pertence a apenas um usuário.

### 💵 Depósito
- Função **positional-only**.
- Aceita apenas valores positivos.
- Atualiza saldo e extrato.
- Mensagens claras de sucesso ou falha.

### 💸 Saque
- Função **keyword-only**.
- Valida:
  - Valor positivo
  - Saldo disponível
  - Limite por saque (R$ 500)
  - Máximo 3 saques
- Atualiza saldo, extrato e contador de saques.
- Mensagens claras de sucesso ou falha.

### 📄 Extrato
- Função **positional e keyword-only**.
- Exibe movimentações e saldo.
- Caso não haja operações, informa que não foram realizadas.

### 🖥️ Experiência do Usuário
- Solicita CPF antes de qualquer operação.
- Lista todas as contas do usuário para escolha.
- Feedback detalhado em todas operações.

---

## 🧩 Estrutura do Código

- **Listas globais**: `usuarios`, `contas`.
- **Funções principais**:
  - `criar_usuario()` – cadastro de cliente com validação
  - `criar_conta()` – criação de conta vinculada
  - `depositar(saldo, valor, extrato)` – positional-only
  - `sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)` – keyword-only
  - `exibir_extrato(saldo, /, *, extrato)` – positional e keyword
  - `listar_contas_usuario(usuario)` – lista contas do usuário
  - `menu_principal()` – interface principal
- **Validações**: CPF, CEP, limite de saques, saldo, valores monetários.
- **Mensagens**: feedback para sucesso e falha.

---

## ⚙️ Tecnologias e Conceitos Aplicados

- **Python 3.x**
- Estruturas de dados: listas e dicionários
- Modularização com funções
- Passagem de argumentos: posicional, keyword-only, positional + keyword
- Validação de dados (CPF, CEP, valores)
- Manipulação de strings e expressões regulares (`re`)
- Boas práticas: funções pequenas e reutilizáveis, mensagens claras, código organizado

---

## 🚀 Como Executar

1. Tenha **Python 3.x** instalado.
2. Clone ou baixe este repositório.
3. Execute o arquivo principal:

```bash
python nome_do_arquivo.py

    Siga o menu interativo para cadastrar usuários, criar contas e realizar operações bancárias.

🎯 Aprendizados e Objetivos

    Modularização e funções avançadas em Python

    Validação de dados e boas práticas de programação

    Interfaces de texto amigáveis e seguras

    Manipulação de listas e dicionários

    Passagem de parâmetros posicional e por nome

    Feedback detalhado para todas operações

📌 Observações

    CPF e CEP são validados e formatados automaticamente.

    Limite de saque por operação: R$ 500.

    Máximo de saques por conta: 3.

    Usuários podem ter múltiplas contas.

    Cada conta pertence a apenas um usuário.

🔗 Referências

    Digital Innovation One – Back-End com Python™

Certificação: Luizalabs – Dominando Funções e Boas Práticas em Python™

Curso: Otimizando o Sistema Bancário com Funções Python™

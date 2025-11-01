import re

# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Função para validar CPF
def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)  # Remove tudo que não for número
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * (i + 1 - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if int(cpf[i]) != digito:
            return False
    return True

# Formata CPF para XXX.XXX.XXX-XX
def formatar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# Formata CEP para XXXXX-XXX
def formatar_cep(cep):
    cep = re.sub(r'[^0-9]', '', cep)
    return f"{cep[:5]}-{cep[5:]}"

# Função para cadastrar usuário
def criar_usuario():
    nome = input("Nome completo: ").strip()
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
    cpf = input("CPF (somente números): ").strip()
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    if not validar_cpf(cpf):
        print("CPF inválido!")
        return
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado!")
        return
    
    endereco = input("Endereço (logradouro, número, bairro, cidade/UF, CEP): ").strip()
    cep_match = re.search(r'\d{5}-?\d{3}', endereco)
    if not cep_match:
        print("CEP inválido! Deve conter 8 números.")
        return
    cep_formatado = formatar_cep(cep_match.group())
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "cpf_formatado": formatar_cpf(cpf),
        "endereco": endereco,
        "cep_formatado": cep_formatado
    })
    print(f"Usuário {nome} cadastrado com sucesso!")

# Função para criar conta
def criar_conta():
    if not usuarios:
        print("Nenhum usuário cadastrado! Cadastre um usuário primeiro.")
        return
    
    cpf = input("Informe o CPF do titular da conta: ").strip()
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print("CPF não encontrado! Cadastre o usuário primeiro.")
        return
    
    numero_conta = len(contas) + 1
    agencia = "0001"
    
    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0
    })
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}, Agência: {agencia}")
    print(f"Titular: {usuario['nome']}, CPF: {usuario['cpf_formatado']}")

# Função de depósito (positional only)
def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Operação falhou! Valor inválido para depósito.")
        return saldo, extrato
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

# Função de saque (keyword only)
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("Operação falhou! Valor inválido para saque.")
        return saldo, extrato, numero_saques
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
        return saldo, extrato, numero_saques
    if valor > limite:
        print("Operação falhou! Valor do saque excede o limite.")
        return saldo, extrato, numero_saques
    if numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato, numero_saques
    
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

# Função de extrato (positional and keyword only)
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Lista de contas do usuário
def listar_contas_usuario(usuario):
    user_contas = [c for c in contas if c['usuario']['cpf'] == usuario['cpf']]
    for c in user_contas:
        print(f"Agência: {c['agencia']} | Conta: {c['numero_conta']} | Saldo: R$ {c['saldo']:.2f}")
    return user_contas

# Menu principal
def menu_principal():
    LIMITE_SAQUES = 3
    limite = 500
    
    while True:
        menu = """
[1] Cadastrar usuário
[2] Criar conta
[3] Depositar
[4] Sacar
[5] Extrato
[6] Sair

=> """
        opcao = input(menu)
        
        if opcao == "1":
            criar_usuario()
        
        elif opcao == "2":
            criar_conta()
        
        elif opcao in ["3", "4", "5"]:
            if not contas:
                print("Nenhuma conta cadastrada! Crie uma conta primeiro.")
                continue
            cpf = input("Informe seu CPF: ").strip()
            cpf = re.sub(r'[^0-9]', '', cpf)
            usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
            if not usuario:
                print("CPF não encontrado!")
                continue
            user_contas = listar_contas_usuario(usuario)
            if not user_contas:
                print("Nenhuma conta cadastrada para este usuário!")
                continue
            numero = int(input("Escolha o número da conta: "))
            conta = next((c for c in user_contas if c["numero_conta"] == numero), None)
            if not conta:
                print("Conta não encontrada!")
                continue
            
            if opcao == "3":
                valor = float(input("Informe o valor do depósito: "))
                conta["saldo"], conta["extrato"] = depositar(conta["saldo"], valor, conta["extrato"])
            elif opcao == "4":
                valor = float(input("Informe o valor do saque: "))
                conta["saldo"], conta["extrato"], conta["numero_saques"] = sacar(
                    saldo=conta["saldo"],
                    valor=valor,
                    extrato=conta["extrato"],
                    limite=limite,
                    numero_saques=conta["numero_saques"],
                    limite_saques=LIMITE_SAQUES
                )
            elif opcao == "5":
                exibir_extrato(conta["saldo"], extrato=conta["extrato"])
        
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        
        else:
            print("Operação inválida! Selecione novamente.")

# Executa o sistema
menu_principal()
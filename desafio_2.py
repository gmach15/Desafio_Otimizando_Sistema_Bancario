# Desafio 2 Python - Otimizando Sistema Bancário

def menu():
    painel = """
    * ================ MENU ================ *
    || [1] Depositar                        ||
    || [2] Sacar                            ||  
    || [3] Extrato                          ||   
    || [4] Novo Usuário                     ||
    || [5] Nova Conta                       ||
    || [6] Listar Contas                    ||
    || [7] Sair                             ||
    * ====================================== *
    => """
    while True:
        try:
            escolha = int(input(painel))
            return escolha
        except ValueError:
            print("Por favor, insira um número válido.")



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor: .2f}\n'
        print('Depósito realizado com sucesso!')
    else:
        print('Operação falhou! O valor informado é inválido.')

    return saldo, extrato

def sacar(saldo, saque, extrato):
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >=LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Saldo insuficiente para o levantamento indicado')

        elif excedeu_limite:
            print('Operação falhou! O valor do levantamento excede o limite diário')

        elif excedeu_saques:
            print('Operação falhou! Númeor máximo de levantamentos excedido.')

        elif saque > 0:
            saldo -= saque
            extrato = f'Levantamento: R$ {saque: .2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! O valor informado é inválido.')

        return saldo, extrato

def imprimirExtrato(saldo, extrato):
        print('\n================== EXTRATO ==================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo: .2f}')
        print('===============================================')

def criarUsuario(usuarios):
        cpf = input('Digite seu CPF(Somente números): ')
        usuario = filtrarUsuarios(cpf, usuarios)

        if usuario in usuarios:
             print('Usuário já cadastrado! Digite novamente')
             return
        
        nome = input('Digite seu nome completo: ')
        dataNascimento = input('Digite sua data de nascimento(somente números): ')
        endereco = input('Digite seu endereço (rua, nº - bairro - cidade/estado): ')
        

        dataFormatada = dataNascimento[:2] + '/' + dataNascimento[2:4 ] + '/' + dataNascimento[4:]
        
        usuarios.append({"nome": nome, "dataNascimento": dataFormatada, "cpf": cpf, "endereco": endereco})

        print('Usuário cadastrado com sucesso!')
      
def filtrarUsuarios(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None

def criarConta(agencia, numeroConta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrarUsuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numeroConta": numeroConta, "usuario": usuario}

    print("Usuário não encontrado, digite novamente!")


def listarContas(contas):
    if not contas: #Verificação da lista de contas
         print('Nenhuma conta aberta no momento.')
    
    else:
        for conta in contas:
            print(
                f"""
                Agência: {conta['agencia']}
                C/C: {conta['numeroConta']}
                Titular: {conta['usuario']['nome']}
            """
        )
            return contas

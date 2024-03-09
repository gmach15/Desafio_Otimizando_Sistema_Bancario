from desafio_2 import *


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 3:
            imprimirExtrato(saldo, extrato=extrato)

        elif opcao == 4:
            criarUsuario(usuarios)
            
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criarConta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == 6:
            listarContas(contas)

        elif opcao == 7:
            print('Operação finalizada!')
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()

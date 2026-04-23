saldo = 0.0
extrato = []

def adicionarDinheiro(valor):
    global saldo
    
    if valor <= 0:
        print('Valor inválido!')
        return
    
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    
    print('Depósito realizado com sucesso!')
    print(f"Saldo atual: R$ {saldo:.2f}")


def sacarDinheiro(valor):
    global saldo
    
    if valor <= 0:
        print('Valor inválido!')
        return
    
    if valor > saldo:
        print('Saldo insuficiente para realizar o saque.')
        return
    
    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    
    print('Saque realizado com sucesso!')
    print(f"Saldo atual: R$ {saldo:.2f}")


def mostrarExtrato():
    print('\n===== EXTRATO =====')
    
    if len(extrato) == 0:
        print('Não foram realizadas movimentações.')
    else:
        for operacao in extrato:
            print(operacao)
    
    print(f"Saldo atual: R$ {saldo:.2f}")


# MENU
opcao = None

while opcao != '4':
    print('\n===== MENU =====')
    print('1 - Adicionar Dinheiro')
    print('2 - Sacar Dinheiro')
    print('3 - Mostrar Extrato')
    print('4 - Sair')
    
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        valor = float(input('Digite o valor do depósito: '))
        adicionarDinheiro(valor)
    
    elif opcao == '2':
        valor = float(input('Digite o valor do saque: '))
        sacarDinheiro(valor)
    
    elif opcao == '3':
        mostrarExtrato()
    
    elif opcao == '4':
        print('Saindo do sistema...')
    
    else:
        print('Opção inválida!')
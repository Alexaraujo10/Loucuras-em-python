# Variável que armazena o saldo atual da conta
saldo = 0.0

# Lista que guarda todas as movimentações (depósitos e saques)
extrato = []


# =========================
# FUNÇÃO: ADICIONAR DINHEIRO
# =========================
def adicionarDinheiro(valor):
    global saldo  # Permite alterar a variável saldo fora da função

    # Verifica se o valor é válido (não pode ser zero ou negativo)
    if valor <= 0:
        print('Valor inválido!')
        return  # Encerra a função

    # Soma o valor ao saldo atual
    saldo += valor

    # Registra a operação no extrato
    extrato.append(f"Depósito: R$ {valor:.2f}")

    # Exibe mensagens para o usuário
    print('Depósito realizado com sucesso!')
    print(f"Saldo atual: R$ {saldo:.2f}")


# =========================
# FUNÇÃO: SACAR DINHEIRO
# =========================
def sacarDinheiro(valor):
    global saldo  # Permite alterar o saldo global

    # Verifica se o valor é válido
    if valor <= 0:
        print('Valor inválido!')
        return

    # Verifica se há saldo suficiente
    if valor > saldo:
        print('Saldo insuficiente para realizar o saque.')
        return

    # Subtrai o valor do saldo
    saldo -= valor

    # Registra a operação no extrato
    extrato.append(f"Saque: R$ {valor:.2f}")

    # Exibe mensagens
    print('Saque realizado com sucesso!')
    print(f"Saldo atual: R$ {saldo:.2f}")


# =========================
# FUNÇÃO: MOSTRAR EXTRATO
# =========================
def mostrarExtrato():
    print('\n===== EXTRATO =====')

    # Verifica se não houve nenhuma movimentação
    if len(extrato) == 0:
        print('Não foram realizadas movimentações.')
    else:
        # Percorre a lista e mostra cada operação
        for operacao in extrato:
            print(operacao)

    # Mostra o saldo atual
    print(f"Saldo atual: R$ {saldo:.2f}")


# =========================
# MENU PRINCIPAL (LOOP)
# =========================

opcao = None

# O programa roda até o usuário escolher sair (opção 4)
while opcao != '4':

    # Exibição do menu
    print('\n===== MENU =====')
    print('1 - Adicionar Dinheiro')
    print('2 - Sacar Dinheiro')
    print('3 - Mostrar Extrato')
    print('4 - Sair')

    # Recebe a opção do usuário
    opcao = input('Escolha uma opção: ')

    # =========================
    # OPÇÃO 1: DEPÓSITO
    # =========================
    if opcao == '1':
        valor = float(input('Digite o valor do depósito: '))
        adicionarDinheiro(valor)

    # =========================
    # OPÇÃO 2: SAQUE
    # =========================
    elif opcao == '2':
        valor = float(input('Digite o valor do saque: '))
        sacarDinheiro(valor)

    # =========================
    # OPÇÃO 3: EXTRATO
    # =========================
    elif opcao == '3':
        mostrarExtrato()

    # =========================
    # OPÇÃO 4: SAIR
    # =========================
    elif opcao == '4':
        print('Saindo do sistema...')

    # =========================
    # OPÇÃO INVÁLIDA
    # =========================
    else:
        print('Opção inválida!')
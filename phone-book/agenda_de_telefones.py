
numeros = {}
contador = 0

print('=' * 86)
print('    AGENDA DE CONTATOS    ')
print('=' * 86)
print('opções disponíveis:  ')
print()    
print('digite 4 para sair')
print('digite 1 para adicionar um contato')
print('digite 3 para remover um contato')
print('digite 2 para listar os contatos')
print('=' * 86)

print('\033[s', end='')

while True:

    escolha = input('digite a opção desejada:  ')

    print('\033[u\033[J', end='', flush=True)

# fecha o programa
    if escolha == '4':
        print('saindo do programa')
        break

#adiciona um contato
    elif escolha == '1':
        nome = input('digite o nome do contato:  ')
        numero = input('digite o número do contato:  ')
        numeros[nome] = numero
        print(f'contato {nome} adicionado com sucesso')

#lista os contatos
    elif escolha == '2':
        if not numeros:
            print('agenda vazia')
        elif nome not in numeros:
            print('contato não encontrado')
        else:
            print('contatos na agenda:  ')
            for nome, numero in numeros.items():
                print(f'{nome}: {numero}')
#remove um contato
    elif escolha == '3':
        nome = input('digite o nome do contato que deseja remover:  ')
        if nome in numeros:
            numeros.pop(nome)
            print(f'contato {nome} removido com sucesso')
        else:
            print('contato não encontrado')

    else:
        print('opção inválida, tente novamente')
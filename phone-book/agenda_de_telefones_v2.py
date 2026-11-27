
numeros = {}
while True:
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
            nome = input('digite o nome do contato:  ').strip()
            numero = input('digite o número do contato:  ').strip()
            if not nome or not numero:
                print('nome e número não podem ficar vazios')
            elif numero not in numeros.values():
                numeros[nome] = numero
                print(f'contato {nome} adicionado com sucesso')

            else:
                print('o número já existe. deseja atualizá-lo?')
                escolha = input('digite "s" para sim e "n" para não: ')
                if escolha == 's':
                    numeros[nome] = numero
                    print('numero atualizado!')
                elif escolha == 'n':
                    print('\033[u\033[J', end='', flush=True)
                    print('voltando ao menu...')
                    
#lista os contatos
        elif escolha == '2':
            if not numeros:
                print('agenda vazia')
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

    if escolha == '4':
        break
    else:
        print('opção inválida.')
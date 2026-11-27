# decide onde fica a tela
def def_tela():
    print('\033[s', end='')
#limpa a tela
def limpa_tela():
    print('\033[u\033[J', end='', flush=True)
# onde armazena os produtos e seus preços
compras = {}
# menu principal
while True:
    print('=' * 86)
    print('    LISTA DE COMPRAS    ')
    print('=' * 86)
    print('opções disponíveis:  ')
    print()    
    print('digite 4 para sair')
    print('digite 1 para adicionar um item')
    print('digite 2 para listar os itens')
    print('digite 3 para remover um item')
    print('=' * 86)

    escolha = input('digite a opção desejada:  ')
# fecha o programa
    if escolha == '4':
        print('saindo do programa')
        break
#adiciona um item
    elif escolha == '1':
        while True:
            print('itens disponíveis para adicionar\n' \
            '1 - melancia - R$10,99\n' \
            '2 - banana - R$5,99\n' \
            '3 - maçã - R$3,99\n' \
            '4 - laranja - R$4,99\n' \
            '5 - tomate - R$2,99\n' \
            '6 - batata - R$1,99\n' \
            '7 - sair\n' \
            )

            item = input('digite o número do item que deseja adicionar:  ')
            def_tela()
            if item == '1':
                compras['melancia'] = 10.99
                print('item melancia adicionado com sucesso')
                limpa_tela()

            elif item == '2':
                compras['banana'] = 5.99
                print('item banana adicionado com sucesso')
                limpa_tela()

            elif item == '3':
                compras['maçã'] = 3.99
                print('item maçã adicionado com sucesso')
                limpa_tela()

            elif item == '4':
                compras['laranja'] = 4.99
                print('item laranja adicionado com sucesso')
                limpa_tela()

            elif item == '5':
                compras['tomate'] = 2.99
                print('item tomate adicionado com sucesso')
                limpa_tela()

            elif item == '6':
                compras['batata'] = 1.99
                print('item batata adicionado com sucesso')
                limpa_tela()
# retorna ao menu principal mas n fecha o programa
            elif item == '7':
                print('voltando ao menu principal')
                limpa_tela()
                break

            else:
                print('opção inválida, tente novamente')
                limpa_tela()
# lista os itens
    elif escolha == '2':
        if not compras:
            print('lista de compras vazia')
        else:
            print('itens na lista de compras:  ')
            for item, preco in compras.items():
                print(f'{item}: R${preco:.2f}\n')
# remove um item
    elif escolha == '3':
        def_tela()

        if not compras:
            print('lista de compras vazia')
            limpa_tela()

        else:
            print('itens na lista de compras:  ')
            for item, preco in compras.items():
                print(f'{item}: R${preco:.2f}\n')
                    
            print('digite o nome do item que deseja remover:  ')
            item = input()
            if item in compras:
                compras.pop(item)
                print(f'item {item} removido com sucesso')
            else:
                print('item não encontrado')
                limpa_tela()

    else:
        print('opção inválida, tente novamente')
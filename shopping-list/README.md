# Lista de Compras — Mercado (`mercado.py`)

Programa interativo de linha de comando escrito em Python que simula uma lista de compras de mercado. O usuário pode adicionar produtos de um catálogo fixo com preços pré-definidos, listar os itens adicionados e removê-los pelo nome, armazenando tudo em memória durante a execução.

## Objetivo

Praticar manipulação de dicionários, funções auxiliares, menus interativos com laços `while True` aninhados, formatação de valores monetários e controle básico de exibição no terminal com sequências ANSI.

## Funcionalidades existentes

- **Menu principal:** apresenta quatro opções ao usuário:
  - `1` — Adicionar um item à lista
  - `2` — Listar os itens da lista de compras
  - `3` — Remover um item da lista
  - `4` — Sair do programa
- **Submenu de produtos (opção `1`):** mantém o usuário em um loop próprio de adição com 6 produtos disponíveis e uma opção de retorno:
  - `1` — `melancia` (R$ 10,99)
  - `2` — `banana` (R$ 5,99)
  - `3` — `maçã` (R$ 3,99)
  - `4` — `laranja` (R$ 4,99)
  - `5` — `tomate` (R$ 2,99)
  - `6` — `batata` (R$ 1,99)
  - `7` — `sair` (volta ao menu principal sem encerrar o programa)
- **Listagem de itens (opção `2`):** informa caso a lista esteja vazia ou exibe cada item salvo em `compras` com o preço formatado com duas casas decimais (`R${preco:.2f}`).
- **Remoção de itens (opção `3`):** verifica se a lista está vazia; se houver itens, exibe os produtos atuais, solicita o nome do item e remove a entrada do dicionário com `.pop(item)` (ou informa `item não encontrado`).
- **Limpeza de mensagens no terminal:** utiliza as funções `def_tela()` (`\033[s`) e `limpa_tela()` (`\033[u\033[J`) para salvar e restaurar a posição do cursor ao exibir confirmações e avisos.

## Tecnologias e conceitos utilizados

- **Python 3** (somente biblioteca padrão, sem dependências externas)
- Funções (`def_tela` e `limpa_tela`)
- Dicionários (`compras = {}`) com atribuição por chave, iteração via `.items()` e remoção via `.pop()`
- Laços `while True` aninhados com `break`
- Estruturas condicionais (`if`, `elif`, `else`)
- Formatação de números decimais com f-strings (`:.2f`)

## Requisitos

- Python 3 instalado no sistema (terminal compatível com sequências de escape ANSI para a limpeza de tela)

## Instalação e execução

1. Acesse a pasta do repositório `python-learning-projects`:

   ```bash
   cd python-learning-projects
   ```

2. Execute o script com Python 3:

   ```bash
   python3 shopping-list/mercado.py
   ```

## Exemplo de uso

```text
======================================================================================
    LISTA DE COMPRAS    
======================================================================================
opções disponíveis:  

digite 4 para sair
digite 1 para adicionar um item
digite 2 para listar os itens
digite 3 para remover um item
======================================================================================
digite a opção desejada:  1
itens disponíveis para adicionar
1 - melancia - R$10,99
2 - banana - R$5,99
3 - maçã - R$3,99
4 - laranja - R$4,99
5 - tomate - R$2,99
6 - batata - R$1,99
7 - sair

digite o número do item que deseja adicionar:  1
digite o número do item que deseja adicionar:  7
digite a opção desejada:  2
itens na lista de compras:  
melancia: R$10.99

digite a opção desejada:  3
itens na lista de compras:  
melancia: R$10.99

digite o nome do item que deseja remover:  
melancia
item melancia removido com sucesso
digite a opção desejada:  4
saindo do programa
```

# Agenda de Contatos (`phone-book`)

Agenda telefônica interativa de linha de comando escrita em Python que armazena contatos (nome e número) em memória utilizando um dicionário. Todas as mensagens e prompts exibidos ao usuário estão em português.

## Arquivos do projeto

- `agenda_de_telefones.py`: versão inicial (v1) da agenda.
- `agenda_de_telefones_v2.py`: segunda versão (v2) com validações, correções de fluxo e tratamento de números duplicados.

## Funcionalidades

- Menu numérico no terminal com quatro opções:
  - `1` — Adicionar um contato
  - `2` — Listar os contatos cadastrados
  - `3` — Remover um contato pelo nome
  - `4` — Sair do programa
- Armazenamento dos pares `nome: numero` em um dicionário (`numeros`).
- Limpeza parcial da saída no terminal usando sequências de escape ANSI (`\033[s` e `\033[u\033[J`) para manter o menu visível.

## Melhorias da v2 (`agenda_de_telefones_v2.py`)

Em relação à primeira versão (`agenda_de_telefones.py`), a v2 traz as seguintes melhorias:

1. **Validação de campos vazios e espaços extras:** aplica `.strip()` no nome e no número digitados e impede o cadastro caso algum dos dois esteja vazio (`nome e número não podem ficar vazios`).
2. **Verificação de número duplicado:** antes de salvar, verifica se o número já existe em `numeros.values()`. Se já existir, pergunta ao usuário (`s` ou `n`) se deseja atualizar o contato ou voltar ao menu.
3. **Correção na listagem de contatos:** removeu a condição `elif nome not in numeros:` que existia na v1 (e que causava erro caso a listagem fosse escolhida antes de `nome` ser definido), passando a listar diretamente os contatos quando a agenda não está vazia.
4. **Controle de fluxo com loops aninhados:** utiliza um loop externo para exibir o menu e um loop interno para processar as opções, garantindo que a opção `4` encerre o programa corretamente.
5. **Limpeza de código:** removeu a variável `contador = 0`, que existia na v1 mas não era utilizada.

## Conceitos praticados

- Dicionários (`dict`): inserção, verificação em `.values()`, iteração com `.items()` e remoção com `.pop()`
- Manipulação e validação de strings com `.strip()`
- Estruturas condicionais (`if`, `elif`, `else`) e operadores de pertencimento (`in`, `not in`)
- Laços `while True` (simples e aninhados) com `break`
- Entrada de dados com `input()`, formatação com f-strings e sequências ANSI no terminal

## Requisitos

- Python 3 (sem dependências externas)

## Como executar

Na raiz do repositório `python-learning-projects`:

```bash
# Versão 1
python3 phone-book/agenda_de_telefones.py

# Versão 2 (recomendada)
python3 phone-book/agenda_de_telefones_v2.py
```

## Exemplo de uso (v2)

```text
======================================================================================
    AGENDA DE CONTATOS    
======================================================================================
opções disponíveis:  

digite 4 para sair
digite 1 para adicionar um contato
digite 3 para remover um contato
digite 2 para listar os contatos
======================================================================================
digite a opção desejada:  1
digite o nome do contato:  Ana
digite o número do contato:  11999990000
contato Ana adicionado com sucesso
digite a opção desejada:  2
contatos na agenda:  
Ana: 11999990000
digite a opção desejada:  4
saindo do programa
```

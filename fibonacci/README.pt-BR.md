[Read in English](./README.md)

# Gerador de Sequência de Fibonacci (`fibonacci.py`)

Script simples em Python para linha de comando que exibe uma sequência numérica no estilo Fibonacci a partir de um número inteiro informado pelo usuário.

## Funcionalidades

- Solicita ao usuário um número inicial (`escreva um número: `) e a quantidade de rodadas (`escreva o numero de rodadas: `).
- Exibe os três primeiros valores calculados (`n`, `n + n` e `n + n1`).
- Executa um laço `for` pelo número de rodadas informado, atualizando e imprimindo dois termos a cada iteração.

## Conceitos praticados

- Leitura de entrada do usuário com `input()`
- Conversão de tipos com `int()`
- Variáveis acumuladoras (`penultimo_n`, `ultimo_n`)
- Operações aritméticas e laço `for` com `range()`

## Requisitos

- Python 3 (sem bibliotecas externas)

## Como executar

```bash
python3 fibonacci/fibonacci.py
```

Exemplo de execução:

```text
escreva um número: 1
escreva o numero de rodadas: 3
1
2
3
5
8
13
21
34
55
```

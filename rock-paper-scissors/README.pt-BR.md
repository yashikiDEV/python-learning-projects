[Read in English](./README.md)

# Pedra, Papel e Tesoura (`pedra_papel_tesoura.py`)

Jogo interativo de Pedra, Papel e Tesoura no terminal escrito em Python, no qual o jogador enfrenta escolhas aleatórias do computador.

## Funcionalidades

- Exibe um menu numerado (`1 - pedra`, `2 - papel`, `3 - tesoura`).
- Gera a jogada do computador aleatoriamente com `random.randint(1, 3)`.
- Avalia o vencedor, empates ou jogadas inválidas por meio da função `resultado(jogador, computador)`.
- Executa em loop contínuo até o jogador digitar `sair` para encerrar o jogo.

## Conceitos praticados

- Uso do módulo padrão `random`
- Constantes (`PEDRA`, `PAPEL`, `TESOURA`)
- Definição de funções com retorno de valor
- Validação de pertencimento com `set`
- Estruturas condicionais (`if`) e laço `while True` com `break`
- Bloco de entrada `if __name__ == "__main__":`

## Requisitos

- Python 3 (sem bibliotecas externas)

## Como executar

```bash
python3 rock-paper-scissors/pedra_papel_tesoura.py
```

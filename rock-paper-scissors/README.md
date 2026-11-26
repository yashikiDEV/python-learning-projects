# Rock, Paper, Scissors (Pedra, Papel e Tesoura)

An interactive terminal Rock, Paper, Scissors game written in Python where the player competes against random computer choices (with prompts and messages in Portuguese).

## Features

- Displays a numbered menu (`1 - pedra`, `2 - papel`, `3 - tesoura`).
- Generates the computer's move randomly using `random.randint(1, 3)`.
- Evaluates the winner, draws, or invalid inputs via the `resultado(jogador, computador)` function.
- Runs continuously in a loop until the player types `sair` to exit.

## Concepts Practiced

- Using the standard `random` module
- Constants (`PEDRA`, `PAPEL`, `TESOURA`)
- Defining functions and returning values
- Membership validation with `set`
- Conditional branching (`if`) and `while True` loops with `break`
- `if __name__ == "__main__":` entry-point guard

## Requirements

- Python 3 (no external libraries required)

## How to Run

```bash
python3 rock-paper-scissors/pedra_papel_tesoura.py
```

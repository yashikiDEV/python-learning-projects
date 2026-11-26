# Fibonacci Sequence Generator

A simple command-line Python script that prints a Fibonacci-style sequence starting from a user-provided integer.

## Features

- Prompts the user (in Portuguese) for a starting number and a number of rounds.
- Prints the first three calculated values (`n`, `n + n`, `n + n1`).
- Runs a `for` loop for the specified number of rounds, updating and printing two terms per iteration.

## Concepts Practiced

- Reading user input with `input()`
- Type conversion with `int()`
- Accumulator variables (`penultimo_n`, `ultimo_n`)
- Arithmetic operations and `for` loops with `range()`

## Requirements

- Python 3 (no external libraries required)

## How to Run

```bash
python3 fibonacci/fibonacci.py
```

Example interaction:

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

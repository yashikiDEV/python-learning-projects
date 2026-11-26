# Python Learning Projects

A collection of beginner Python scripts created while practicing fundamental programming concepts, standard library modules, and command-line interaction.

## Educational Goal

This repository serves as a hands-on record of foundational Python exercises, focusing on:

- User input handling and type conversion
- Control flow (`if` conditions, `for` and `while` loops)
- Functions and modular logic
- Working with built-in standard library modules (`random`, `json`)
- Reading and writing local files

## Projects

| Folder | Script | Description |
| --- | --- | --- |
| [`fibonacci/`](./fibonacci) | `fibonacci.py` | Generates a Fibonacci-style number sequence from a starting integer and number of rounds. |
| [`rock-paper-scissors/`](./rock-paper-scissors) | `pedra_papel_tesoura.py` | Interactive command-line Rock, Paper, Scissors game against the computer (prompts in Portuguese). |
| [`json-file-creator/`](./json-file-creator) | `json_teste_.py` | Writes a Python dictionary to `teste.json` and reads it back from disk. |

## Technologies

- **Python 3** (tested with Python 3.12)
- Python Standard Library only (`random`, `json`) — no external dependencies required.

## Repository Structure

```text
python-learning-projects/
├── .gitignore
├── README.md
├── fibonacci/
│   ├── README.md
│   └── fibonacci.py
├── json-file-creator/
│   ├── README.md
│   └── json_teste_.py
└── rock-paper-scissors/
    ├── README.md
    └── pedra_papel_tesoura.py
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yashikiDEV/python-learning-projects.git
   cd python-learning-projects
   ```

2. Run any project using `python3`:

   ```bash
   python3 fibonacci/fibonacci.py
   python3 rock-paper-scissors/pedra_papel_tesoura.py
   ```

   For the JSON script, run it from inside its folder so `teste.json` is created there:

   ```bash
   cd json-file-creator
   python3 json_teste_.py
   ```

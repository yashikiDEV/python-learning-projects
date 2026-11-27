[Leia em português](./README.pt-BR.md)

# JSON File Creator

A small Python script that demonstrates how to serialize a Python dictionary to a `.json` file and load it back using the built-in `json` module.

## Features

- Defines a sample dictionary (`nome`, `idade`, `cidade`).
- Writes the dictionary to `teste.json` in the current working directory using `json.dump()` with `ensure_ascii=False` and `indent=4`.
- Reopens `teste.json` using a `with` context manager, parses it with `json.load()`, and prints the resulting dictionary.

## Concepts Practiced

- Built-in `json` module (`json.dump` and `json.load`)
- Python dictionaries
- File handling (`open()`, `close()`, and `with open(...)` context managers)
- UTF-8 encoding (`encoding="utf-8"`) and pretty-printed JSON output

## Requirements

- Python 3 (no external libraries required)

## How to Run

Run the script from inside the `json-file-creator/` directory:

```bash
cd json-file-creator
python3 json_teste_.py
```

Running it creates `teste.json` in the current directory and prints the loaded dictionary to the terminal.

# Phone Book (Agenda de Contatos)

An interactive command-line phone book written in Python that stores contacts in memory using a dictionary (with prompts and messages in Portuguese).

## Features

- Displays a numbered menu (`1` to add a contact, `2` to list contacts, `3` to remove a contact, `4` to exit).
- Adds contacts by storing name (`nome`) and phone number (`numero`) pairs in a dictionary.
- Lists saved contacts or reports when the phone book is empty.
- Removes an existing contact by name, or notifies if the contact is not found.
- Uses ANSI escape sequences to clear previous interaction output while keeping the menu visible.

## Concepts Practiced

- Dictionaries (`dict`) for storing key-value pairs and iterating with `.items()`
- Removing entries with `.pop()` and membership checks (`in` / `not in`)
- Conditional branching (`if` / `elif` / `else`) and `while True` loops with `break`
- Terminal input with `input()` and string formatting with f-strings

## Requirements

- Python 3 (no external libraries required)

## How to Run

```bash
python3 phone-book/agenda_de_telefones.py
```

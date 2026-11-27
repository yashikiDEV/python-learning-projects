[Read in English](./README.md)

# Criador de Arquivo JSON (`json_teste_.py`)

Pequeno script em Python que demonstra como serializar um dicionário Python para um arquivo `.json` e carregá-lo de volta usando o módulo embutido `json`.

## Funcionalidades

- Define um dicionário de exemplo com os campos `nome`, `idade` e `cidade`.
- Grava o dicionário em `teste.json` no diretório de trabalho atual usando `json.dump()` com `ensure_ascii=False` e `indent=4`.
- Reabre `teste.json` usando um gerenciador de contexto `with`, faz a leitura com `json.load()` e imprime o dicionário resultante.

## Conceitos praticados

- Módulo padrão `json` (`json.dump` e `json.load`)
- Dicionários em Python
- Manipulação de arquivos (`open()`, `close()` e `with open(...)`)
- Codificação UTF-8 (`encoding="utf-8"`) e formatação legível de JSON (`indent=4`)

## Requisitos

- Python 3 (sem bibliotecas externas)

## Como executar

Execute o script dentro da pasta `json-file-creator/`:

```bash
cd json-file-creator
python3 json_teste_.py
```

Ao executar, o arquivo `teste.json` é criado no diretório atual e o dicionário carregado é exibido no terminal.

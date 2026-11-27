# Projetos de Aprendizado em Python (`python-learning-projects`)

Coleção de scripts e pequenos programas em Python desenvolvidos durante o aprendizado de conceitos fundamentais de programação, módulos da biblioteca padrão e interação por linha de comando.

## Objetivo educacional

Este repositório registra a evolução prática em exercícios introdutórios de Python, com foco em:

- Leitura de dados do usuário e conversão de tipos
- Controle de fluxo (`if`/`elif`/`else`, laços `for` e `while`)
- Funções e organização lógica
- Uso de estruturas de dados nativas (como dicionários e conjuntos)
- Uso de módulos da biblioteca padrão (`random`, `json`)
- Leitura e escrita de arquivos locais

## Projetos

| Pasta | Script(s) | Descrição |
| --- | --- | --- |
| [`fibonacci/`](./fibonacci) | `fibonacci.py` | Gera uma sequência numérica no estilo Fibonacci a partir de um inteiro inicial e da quantidade de rodadas. |
| [`rock-paper-scissors/`](./rock-paper-scissors) | `pedra_papel_tesoura.py` | Jogo interativo de Pedra, Papel e Tesoura no terminal contra o computador. |
| [`json-file-creator/`](./json-file-creator) | `json_teste_.py` | Grava um dicionário Python no arquivo `teste.json` e o lê de volta do disco. |
| [`phone-book/`](./phone-book) | `agenda_de_telefones.py`, `agenda_de_telefones_v2.py` | Agenda de contatos interativa no terminal que adiciona, lista e remove contatos em memória (v1 e v2 com validações e verificação de duplicidade). |
| [`shopping-list/`](./shopping-list) | `mercado.py` | Lista de compras de mercado interativa no terminal com catálogo fixo de produtos, preços e remoção por nome. |

## Tecnologias

- **Python 3** (testado com Python 3.12)
- Apenas biblioteca padrão do Python (`random`, `json`) — sem dependências externas.

## Estrutura do repositório

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
├── phone-book/
│   ├── README.md
│   ├── agenda_de_telefones.py
│   └── agenda_de_telefones_v2.py
├── rock-paper-scissors/
│   ├── README.md
│   └── pedra_papel_tesoura.py
└── shopping-list/
    ├── README.md
    └── mercado.py
```

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/yashikiDEV/python-learning-projects.git
   cd python-learning-projects
   ```

2. Execute qualquer projeto usando `python3`:

   ```bash
   python3 fibonacci/fibonacci.py
   python3 phone-book/agenda_de_telefones_v2.py
   python3 rock-paper-scissors/pedra_papel_tesoura.py
   python3 shopping-list/mercado.py
   ```

   Para o script de JSON, execute-o de dentro da própria pasta para que o arquivo `teste.json` seja criado no local esperado:

   ```bash
   cd json-file-creator
   python3 json_teste_.py
   ```

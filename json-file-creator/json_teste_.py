import json

teste = {
    "nome": "pedro",
    "idade": 33,
    "cidade": "uberlandia"
}

arquivo = open("teste.json", "w", encoding="utf-8")
json.dump(teste, arquivo, ensure_ascii=False, indent=4)
arquivo.close()


with open("teste.json", "r", encoding="utf-8") as arquivo:
    teste = json.load(arquivo)
    print(teste)

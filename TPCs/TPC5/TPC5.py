import re
import json


file_conceitos = open("conceitos_v2.json", encoding="utf-8")
file_livro = open("LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="utf-8")

texto = file_livro.read()
conceitos = json.load(file_conceitos)

blacklist = ["e", "de", "para", "pelo", "os", "são", "este"]

conceitos_min = {chave.lower(): conceitos[chave] for chave in conceitos}

def etiquetador(matched):
    palavra = matched[0]
    original = palavra
    palavra = palavra.lower()
    if palavra in conceitos_min and palavra not in blacklist:
        descricao = conceitos_min[palavra]
        desc = descricao['desc']
        eng = descricao['en']
        etiqueta = f"<meta charset='UTF-8'><a style='color: slateblue;' href='' title='Definição: {desc} / Tradução: {eng}'>{original}</a>"
        return etiqueta
    else:
        return original

expressao = r'[\wáéçãóõéíêâú]+'
texto = re.sub(expressao, etiquetador, texto, flags=re.IGNORECASE)
texto = re.sub(r'\n',r'<br>', texto)
texto = re.sub(r'\f', r'<hr>', texto)

file_out = open("livro.html", "w", encoding="utf-8")
print(texto, file=file_out)
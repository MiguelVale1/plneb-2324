import re
from gensim.models import Word2Vec
from gensim.utils import tokenize

f2 = open("Harry_Potter_e_A_Pedra_Filosofal.txt", 'r', encoding='utf-8')
f1 = open('Harry_Potter_Camara_Secreta-br.txt', 'r', encoding='utf-8')
harry_text = f1.read()


linhas = harry_text.split("\n")

tokens = []
for linha in linhas:
    linha = re.sub(r'[-!?.,]', r'', linha)
    linha = list(tokenize(linha, lower=True))
    tokens.append(linha)

model = Word2Vec(tokens, vector_size=300, window=20, min_count=7, epochs=20)

print(model.wv.most_similar("dobby"))

model = Word2Vec(tokens, vector_size=400, window=20, min_count=1, epochs=20)

analogia = model.wv["draco"] - model.wv["harry"] + model.wv["grifinória"]
resultado = model.wv.similar_by_vector(analogia)
print(resultado)
import spacy
import numpy as np

nlp = spacy.load("es_core_news_md")

database = [
    "Asesinatos por parte de Carlos Ibañez del Campo.",
    "Nace Madonna.",
    "Blue Ballet.",
    "Las locas en plaza de armas.",
    "Operaciones de reasignación de sexo.",
    "Chicos Rafaela Carrá.",
    "Detenidxs y desaparecidxs trans.",
    "Primero organización política LGTBIAQ+ en Chile: Colectiva lésbica feminista ayuquelén.",
    "Muerte de Edmundo Rodriguez, primer paciente registrado.",
    "Corporación chilena de prevención del SIDA (Acción gay).",
]
tokens = []
A = np.zeros((len(database),len(database)))
for i in database:
    tokens.append(nlp(i))

for t1 in range(len(tokens)):
    for t2 in range(len(tokens)):
        A[t1][t2] = tokens[t1].similarity(tokens[t2])

print(A)


# References
# Spicy – Similarity: https://spacy.io/usage/vectors-similarity
# Numpy: https://www.programiz.com/python-programming/matrix 
# TODO: learn t-sne
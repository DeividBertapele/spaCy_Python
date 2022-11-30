from spacy import blank


nlp = blank ('pt')

doc = nlp('Python é muito massa!!!')

token =  doc[0] # Mostra Python

token1 =  doc[3] # Mostra Python

span = doc[:2] # Mostra Python é


print(token)
print(token1)
print(span)
from spacy import load # carrega um modelo

#pt_core_news_sm => Small (Pequeno)
#pt_core_news_md => Medium (Médio)
#pt_core_news_lg => Large (Grande)

texto = "Python, já tem nova versão 3.11"

nlp = load('pt_core_news_sm')

doc = nlp(texto)

doc.sents

for sent in doc.sents:
    print(sent)
    
    
    
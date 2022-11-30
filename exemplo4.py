from spacy import load, displacy 

#pt_core_news_sm => Small (Pequeno)
#pt_core_news_md => Medium (Médio)
#pt_core_news_lg => Large (Grande)

nlp = load('pt_core_news_sm')

doc = nlp("Python ja tem nova versão 3.11")

# displacy.serve(doc)


for token in doc:
    print('{:10} | {:10} | {:10} | {:10} | {:10} | {}'.format(
            token.text,
            token.pos_,
            token.lemma_,
            token.dep_,
            token.is_stop,
            token.morph))
    
    
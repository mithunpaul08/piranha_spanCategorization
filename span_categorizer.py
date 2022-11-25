import spacy
nlp=spacy.load('en_core_web_trf')
doc=nlp("this is a sentence")
for token in doc:
    print(token.text)
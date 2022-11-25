import spacy
nlp=spacy.load('en_core_web_trf')
doc=nlp("this is a sentence")
print(doc.vocab.strings["coffee"])
print(doc.vocab.strings[3197928453018144401])

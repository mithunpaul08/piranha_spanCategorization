import spacy
nlp=spacy.load('en_core_web_trf')

texts=["what is this","Washington said that","Mark Zuckerberg is the owner of Meta"]

for doc in nlp.pipe(texts):
    print([(ent.text, ent.label_) for ent in doc.ents])
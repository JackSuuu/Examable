import spacy
nlp = spacy.load("en_core_web_lg")
list1 = []

txt1 = "This is the way I gonna die"
txt2 = "This is the way I gonna die or live"

doc1 = nlp(txt1)
doc2 = nlp(txt2)

list1.append(doc1.similarity(doc2))

print(list1)

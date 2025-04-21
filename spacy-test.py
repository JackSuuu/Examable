import spacy
import string

nlp = spacy.load('en_core_web_sm')

txt1 = "By using a suitable substitution, solve the equation􏰄2x − 3􏰅2 − 4 − 3 = 0."
txt2 = "For the general case in which angle BAC = 􏰀 radians, where 0 < 􏰀 < 1π, it is given that 􏰀 > 1.Find the set of possible values of k."

doc1 = nlp(txt1)
doc2 = nlp(txt2)

list1 = []
list2 = []
list3 = []
count = 0

for token in doc1:
    token = token.lemma_
    if token not in string.punctuation:
        list1.append(token)

for token in doc2:
    token = token.lemma_
    if token not in string.punctuation:
        list2.append(token)


if count == 0:
    set1 = set(list1)
    set2 = set(list2)
    set3 = (set1 and set2)
    list3.append(set3)
    print(list3)








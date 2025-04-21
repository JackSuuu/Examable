import spacy
nlp = spacy.load('en_core_web_sm')
text = "This is first sentence.\nNext is numbered list.\n1. Hello World!\n2. Hello World2!\n3. Hello World!"

text_sentences = nlp(text)

for sentence in text_sentences.sents:
    print(sentence.text)
import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    doc = nlp("u"+sentences)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            sentences = sentences.replace(ent.text, "X"*len(ent.text))
    return sentences


print(anonymize_text("Mark Cavendish ate an apple"))
# 'John ate an apple'
# 'John ate an apple Oh John'
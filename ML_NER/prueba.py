import re
import json
import spacy
from spacy.lang.es import Spanish
from spacy.pipeline import EntityRuler
from spacy import displacy

# nlp = Spanish()
nlp = spacy.load("es_core_news_sm",  disable = ['ner'])
def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

patterns = load_data("patterns.json")
@Spanish.component("Medicina")
def medicina_component(doc):
    ruler = EntityRuler(nlp)
    for pattern in patterns:
        ruler.add_patterns([pattern])
    doc.ents = ruler(doc).ents
    return doc

nlp.add_pipe("Medicina", last=True)
nlp.to_disk("Medicina2")
print(nlp.pipe_names)

textos = load_data("data/textos.json")
text = textos[7].lower()

doc = nlp(text)
results=[]
for ent in doc.ents:
    results.append(ent.text)

print(doc.ents)

colors = {"Medicina": "#F67DE3", "Enfermedad": "#7DF6D9", "Condición Medica":"#a6e22d", "Musculos":"#f92672", "Patogenos":"#66d9ef", "Organos":"#fd971f"}
options = {"colors": colors} 

displacy.serve(doc,options =options, style="ent")
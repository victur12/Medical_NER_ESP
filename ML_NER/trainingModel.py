import json
import spacy
from spacy.lang.es import Spanish
from spacy.pipeline import EntityRuler

nlp = spacy.load("es_core_news_sm",  disable = ['ner'])


def save_data(file, data):
    with open (file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


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


data = load_data("data/textos2.json")

def test_model_Traning(model, text):
    doc = nlp(text)
    results = []
    entities = []
    for ent in doc.ents:
        entities.append((ent.start_char, ent.end_char, ent.label_))
    if len(entities) > 0:
        results = [text, {"entities": entities}]
        return (results)
    

results = []
entities = []
TRAIN_DATA = []
for text in data:
    resultados = test_model_Traning(nlp, text)
    TRAIN_DATA.append(resultados)


save_data("TRAIN_DATA_MEJORADA.json", TRAIN_DATA)


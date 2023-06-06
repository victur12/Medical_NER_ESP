import random
import json
import spacy
from spacy.training import Example


def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def train(data, iterations):
    TRAIN_DATA = data
    nlp = spacy.blank("es")
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            print("Starting iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                example = Example.from_dict(nlp.make_doc(text), annotations)
                nlp.update(
                    [example],
                    drop=0.4,
                    sgd=optimizer,
                    losses=losses
                )
            print(losses)
    return nlp

TRAIN_DATA = load_data("TRAIN_DATA_MEJORADA.json")
print(type(TRAIN_DATA))

nlp = train(TRAIN_DATA, 47)

nlp.to_disk("MedicinaNER_MODEL_MEJORADA")
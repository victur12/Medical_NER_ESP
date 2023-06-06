import re
import json
import spacy
from spacy.lang.es import Spanish
from spacy.pipeline import EntityRuler
from spacy.lang.es.stop_words import STOP_WORDS
from spacy.lang.es import Spanish
nlp = Spanish()

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)

def save_data(file, data):
    with open (file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


patron = r"[0-9!@#$%^/&*(),.?\":{}|<>]"

def generate_better_list(file):
    data = load_data(file)
    new_list = []
    for item in data:
        new_item = re.sub(patron, "", item)
        new_list.append(new_item)  # Agregar el item original
        new_list.append(new_item.lower())  # Convertir a minúsculas
        new_list.append(new_item.upper())  # Convertir a mayúsculas
        new_list.append(new_item.capitalize())  # Convertir primera letra en mayúscula    
    return (new_list)

def create_training_data(file, type):
    data = generate_better_list(file)
    patterns = []
    for item in data:
        pattern = {
                    "label": type,
                    "pattern": item
                    }
        patterns.append(pattern)
    return (patterns)

dataset = create_training_data("data/medicamentos.json", "Medicina")
dataset += create_training_data("data/enfermedades.json", "Enfermedad")
dataset += create_training_data("data/CondicionMedica.json", "Condición Medica")
dataset += create_training_data("data/musculos.json", "Musculos")
dataset += create_training_data("data/Patogenos.json", "Patogenos")
dataset += create_training_data("data/organos.json", "Organos")
dataset += create_training_data("data/sistema.json", "Sistema")
dataset += create_training_data("data/terapia.json", "Terapia")

@Spanish.component("Medicina")
def my_component(dataset):
    ruler = EntityRuler(nlp)
    return ruler.add_patterns(dataset)

save_data("patterns.json", dataset)

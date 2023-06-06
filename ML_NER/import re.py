import re
import json

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
        new_list.append(new_item)  # Convertir a minúsculas
    return (new_list)

save_data("data/medicamentos2.json", generate_better_list("data/medicamentos.json"))
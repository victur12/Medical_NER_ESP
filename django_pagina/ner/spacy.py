import spacy
from django.conf import settings


def load_spacy_model():
    model_name = settings.SPACY_SETTINGS['model']
    return spacy.load(model_name)

spacy_model = load_spacy_model()

from django.shortcuts import render
from spacy import displacy
from django.http import JsonResponse
from .spacy import spacy_model



# Create your views here.
def home(request):
    text = request.GET.get('text', '')
    doc = spacy_model(text)
    
    colors = {"Medicina": "#F67DE3", "Enfermedad": "#7DF6D9", "Condición Medica":"#a6e22d", "Musculos":"#f92672", "Patogenos":"#66d9ef", 
            "Organos":"#fd971f", "Terapia":"#FFE79B", "Sistema":"#FF5733"}
    options = {"colors": colors} 
    html = displacy.render(doc, style='ent', options=options)
    return render(request, 'home.html', {'html': html})


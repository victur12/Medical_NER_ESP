import spacy
from spacy import displacy

nlp = spacy.load("MedicinaNER_MODEL")
doc = nlp("La fibromialgia es un trastorno crónico que afecta los tejidos blandos y causa dolor generalizado en los músculos. Los pacientes con fibromialgia a menudo experimentan fatiga, dificultad para dormir y problemas de concentración. Para aliviar los síntomas, se pueden recetar medicamentos como pregabalina, un fármaco utilizado para tratar el dolor neuropático. Sin embargo, es importante tener en cuenta que la fibromialgia no es causada por un patógeno específico, sino que se cree que es el resultado de una combinación de factores genéticos, ambientales y neuroquímicos. Aunque no se conoce un virus o bacteria responsable de la fibromialgia, algunas personas con enfermedades autoinmunes, como la esclerosis múltiple, pueden experimentar síntomas similares debido a la inflamación crónica causada por el ataque del sistema inmunológico a los tejidos propios. Es crucial que los pacientes con fibromialgia reciban un enfoque integral de tratamiento que incluya no solo medicamentos, sino también terapia física, ejercicio regular y técnicas de manejo del estrés. Además, es fundamental que se descarten otras condiciones médicas subyacentes que puedan estar contribuyendo a los síntomas. Consultar con un médico especializado en el tratamiento de la fibromialgia puede ayudar a diseñar un plan de tratamiento personalizado y mejorar la calidad de vida de los pacientes.")

from spacy import displacy 

colors = {"Medicina": "#F67DE3", "Enfermedad": "#7DF6D9", "Condición Medica":"#a6e22d", "Musculos":"#f92672", "Patogenos":"#66d9ef", "Organos":"#fd971f"}
options = {"colors": colors} 

displacy.serve(doc, style="ent", options=options)
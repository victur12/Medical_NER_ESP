import spacy
from stop_words import get_stop_words
from heapq import nlargest


stop_words = get_stop_words('es')

nlp = spacy.load("es_core_news_sm")

text = "La concentración de un antimicrobiano en los tejidos y fluidos corporales va a determinar su efecto farmacológico o toxicológico. Por otro lado, la concentración del antimicrobiano en el sitio de infección va determinar su efecto terapéutico. Estos dos aspectos, relacionados con la concentración de los antimicrobianos en los tejidos y su efectos, son los evaluados por la farmacodinamia. En farmacodinamia se evalúa la eficacia terapéutica en base a la relación entre la concentración plasmática del antibiótico y la CIM del microoganismo a ese antimicrobiano. Desde el punto de vista del compartimento central se describen dos modelos de acción de los antimicrobianos, aquellos que son concentración dependiente (su acción se relaciona a la concentración plasmática) y aquellos que son tiempo dependiente (su acción se relaciona al tiempo en que ellos están presentes en concentraciones superiores a la CIM). Entre los primeros destacan dos modelos íntimamente relacionados"
def text_summarizer(raw_docx):
    raw_text = raw_docx
    docx = nlp(raw_text)
    stopwords = list(stop_words)
    # Build Word Frequency
# word.text is tokenization in spacy
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    # Sentence Tokens
    sentence_list = [ sentence for sentence in docx.sents ]

    # Calculate Sentence Score and Ranking
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    # Find N Largest
    summary_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summary_sentences ]
    summary = ' '.join(final_sentences)
    print("Original Document\n")
    print(raw_docx)
    print("Total Length:",len(raw_docx))
    print('\n\nSummarized Document\n')
    print(summary)
    print("Total Length:",len(summary))
    
text_summarizer(text)

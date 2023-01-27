import spacy
from spacy.matcher import Matcher
from gensim.parsing.preprocessing import remove_stopwords
import PyPDF2



def extract_text_from_pdf(pdf_file):
    # Open the PDF file of your choice
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
 
        pdf_text = ' '.join(pdf_text)
        
        return pdf_text  

def clean_data(pdf):
    text = pdf.replace("‘","'")
    text = text.replace("’","'")
    text = text.replace("\n"," ")
    text = remove_stopwords(text) #remove stopwords 
    return text

appleText = extract_text_from_pdf('EULA_Examples\Apple_EULA.pdf')



verbLemmas = ["do", "sell", "retain", "use"]

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

pattern = [
            {"POS" : "PROPN", "OP" : "+"},
            {"IS_ALPHA" : True, "OP" : "+"},
            {"IS_PUNCT" : True, "OP" : "*"},
            {"POS" : "VERB" , "LEMMA" : {"IN" : verbLemmas}},
            {"IS_ALPHA" : True, "OP" : "+"}
             ]

matcher.add("PROPER_NOUNS_AND_VERBS", [pattern], greedy='LONGEST')

doc = nlp(appleText)

matches = matcher(doc)

matches.sort(key = lambda x: x[1])


for match in matches:
    print(doc[match[1] : match [-1]])


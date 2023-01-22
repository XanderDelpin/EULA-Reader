import spacy
import PyPDF2
#import string
from gensim.parsing.preprocessing import remove_stopwords

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
    
nlp = spacy.load("en_core_web_lg")

extract_text1 = extract_text_from_pdf('Text_for_testing.pdf') # VTech Communications, Inc. Privacy Policy
extract_text2 = extract_text_from_pdf('Text_for_testing_2.pdf') # Facebook (Meta) Privacy Policy
extract_text3 = extract_text_from_pdf('Text_for_testing_3.pdf') # Apple Privacy Policy
extract_JungleBook = extract_text_from_pdf('The_Jungle_Book_.pdf') # The Jungle Book book (literature)

extract_text1 = clean_data(extract_text1)
extract_text2 = clean_data(extract_text2)
extract_text3 = clean_data(extract_text3)
extract_JungleBook = clean_data(extract_JungleBook)

doc1 = nlp(extract_text1)
doc2 = nlp(extract_text2)
doc3 = nlp(extract_text3)
doc_JB = nlp(extract_JungleBook)

print("doc1 & doc2: ", doc1.similarity(doc2))
print("doc1 & doc3: ", doc1.similarity(doc3))
print("doc2 & doc3: ", doc2.similarity(doc3))
print("doc1 & doc_JB: ", doc1.similarity(doc_JB))
print("doc2 & doc_JB: ", doc2.similarity(doc_JB))
print("doc3 & doc_JB: ", doc3.similarity(doc_JB))

# Before cleaning data
# output doc1 & doc2: 0.9692745954064461
# output doc1 & doc3: 0.9856110106158126
# output doc2 & doc3: 0.9871303239913188
# output doc2 & Jungle Book: 0.8643944852599666

# After cleaning data
# output doc1 & doc2: 0.9599053198171683
# output doc1 & doc3: 0.9705241678800105
# output doc2 & doc3: 0.9793579897294816
# output doc2 & Jungle Book: 0.6732221021613455
# output Jungle Book & doc2: 0.5904939603892637
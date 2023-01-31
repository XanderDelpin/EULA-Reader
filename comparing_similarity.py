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


# DO NOTE: EULA AND PRIVACY POLICY IS USED INTERCHANGEABLY FOR THE MOMENT...

extract_text1 = extract_text_from_pdf('EULA_Examples\VTech_EULA.pdf')            # VTech Communications, Inc. Privacy Policy
extract_text2 = extract_text_from_pdf('EULA_Examples\Meta_EULA.pdf')             # Facebook (Meta) Privacy Policy
extract_text3 = extract_text_from_pdf('EULA_Examples\Apple_EULA.pdf')            # Apple Privacy Policy
extract_text4 = extract_text_from_pdf('EULA_Examples\Twitter_EULA.pdf')          # Twitter Privacy Policy
extract_text5 = extract_text_from_pdf('EULA_Examples\codeCademy_EULA.pdf')       # CodeCademy Privacy Policy
extract_JungleBook = extract_text_from_pdf('EULA_Examples\The_Jungle_Book_.pdf') # The Jungle Book book (literature)

extract_text1 = clean_data(extract_text1)
extract_text2 = clean_data(extract_text2)
extract_text3 = clean_data(extract_text3)
extract_text4 = clean_data(extract_text4)
extract_text5 = clean_data(extract_text5)
extract_JungleBook = clean_data(extract_JungleBook)

vtechEULA = nlp(extract_text1)            # VTech EULA
metaEULA = nlp(extract_text2)             # Facebook EULA
appleEULA = nlp(extract_text3)            # Apple EULA
twitterEULA = nlp(extract_text4)          # Twitter EULA
codeCademyEULA = nlp(extract_text5)       # CodeCademy EULA
theJungleBook = nlp(extract_JungleBook)   # The Jungle Book

# print("vtechEULA & metaEULA: ", vtechEULA.similarity(metaEULA))
# print("vtechEULA & appleEULA: ", vtechEULA.similarity(appleEULA))
# print("metaEULA & appleEULA: ", metaEULA.similarity(appleEULA))
# print("twitterEULA & appleEULA: ", twitterEULA.similarity(appleEULA))             # NEW
# print("twitterEULA & metaEULA: ", twitterEULA.similarity(metaEULA))               # NEW
# print("twitterEULA & codeCademyEULA: ", twitterEULA.similarity(codeCademyEULA))   # NEW
# print("vtechEULA & the Jungle Book: ", vtechEULA.similarity(theJungleBook))
# print("metaEULA & the Jungle Book: ", metaEULA.similarity(theJungleBook))
# print("appleEULA & the Jungle Book: ", appleEULA.similarity(theJungleBook))
# print("twitterEULA & the Jungle Book: ", twitterEULA.similarity(theJungleBook))   # NEW


# Before cleaning data
# output vtechEULA & metaEULA:          0.9692745954064461
# output vtechEULA & appleEULA:         0.9856110106158126
# output metaEULA & appleEULA:          0.9871303239913188
# output metaEULA & Jungle Book:        0.8643944852599666

# After cleaning data
# output vtechEULA & metaEULA:          0.9599053198171683
# output vtechEULA & appleEULA:         0.9705241678800105
# output metaEULA & appleEULA:          0.9793579897294816
# output twitterEULA & appleEULA:       0.9879862636000314   NEW
# output twitterEULA & metaEULA:        0.9874947449936594   NEW
# output twitterEULA & codeCademyEULA:  0.986048402407567    NEW
# output vtechEULA & the Jungle Book:   0.5904939603892637
# output metaEULA & Jungle Book:        0.6732221021613455
# output Jungle Book & metaEULA:        0.5904939603892637
# output appleEULA & the Jungle Book:   0.6403303658076122
# output twitterEULA & the Jungle Book: 0.6736736358520159   NEW

#NOTE: PRIVACY POLICIES APPEAR TO BE AT LEAST 96% SIMILAR TO EACH OTHER DUE TO CONTEXT



#COMPARING SIMILARITIES - TEST ALEXANDER - COMMIT
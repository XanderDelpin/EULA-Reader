import spacy
import PyPDF2
#import string

#This is a test.........

# Extracting text from PDF file
def extract_text_from_pdf(pdf_file):
    # Open the PDF file of your choice
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        # no_pages = len(reader.pages)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
 
        pdf_text = ' '.join(pdf_text) ### added later check !!!!! Change from list to str
        
        return pdf_text  

# Remove special characters from text    
def clean_data(doc):
    #removed_text = "".join(i for i in doc if i.isalnum())     
    removed_text = doc.replace('.',"")            
    return removed_text

# Write text to file 
def writing_to_file(text, dep):    
    with open("Test_file.txt", "a") as file:
        file.write(text)
        file.write(" ")
        file.write(dep)
        file.write('\n')
    
    # file = open("Test_file.txt", "w") #"a"
    # file.write('\n')
    # file.write(doc)
    # file.close

# Getting text from PDF file    
def getting_from_file(pdf_file):
    with open(pdf_file, "r") as f:
        text = f.read()    
    return text
    
def main():
    # Create a test file
    import os
    
    if os.path.exists("Test_file.txt"):
        os.remove("Test_file.txt")
    
    # Load spacy pipeline
    nlp = spacy.load('en_core_web_lg') #en_core_web_sm
    
    # Get text from PDF
    extracted_text = extract_text_from_pdf('Text_for_testing.pdf')

    # Create NLP object with text from PDF
    doc = nlp(extracted_text) 

    # Write to file word and DEP token
    # Dep: Syntactic dependency, i.e. the relation between tokens
    # DEP = dependencies
    for token in doc:
        writing_to_file(token.text, token.dep_)
    
    #writing_to_file(doc.text)
    
    # doc = nlp("In the event that you choose to make an inquiry or engage in a transaction " +
    #           "while accessing our Sites, we will ask that you provide certain personal information (PI)" + 
    #           "that is needed to respond to the inquiry or complete the transaction.")    
            
main()
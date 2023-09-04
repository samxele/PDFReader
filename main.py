from PyPDF2 import PdfReader
import pyttsx3

'''
Welcome to Sam's PDF Reader. In order for this program to work, please import a pdf file.
'''
engine = pyttsx3.init()

pdfName = input("Enter name of PDF. Include .pdf: ")
reader = PdfReader(pdfName)
numberOfPages = len(reader.pages)
x = 0
while x <= numberOfPages:
    page = reader.pages[x]
    text = page.extract_text()
    engine.say(text)
    engine.runAndWait()
    x += 1



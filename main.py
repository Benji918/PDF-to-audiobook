# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
path = open('/Your pdf dile path/', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.getPage(34)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()


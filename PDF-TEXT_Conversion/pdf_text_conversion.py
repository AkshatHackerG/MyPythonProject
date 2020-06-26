import string
import pdfminer
# To convert simple, text-based PDF file into readable text in python
import PyPDF2
# To convert non-readable, scanned pdf file into readable text in python
import textract
# To clean and convert phrases into keywords
from nltk.tokenize import word_tokenize
# To stops useless words to get converted
from nltk.corpus import stopwords

# enter file name
file_name = input("Enter the pdf-file name: ")
# opens a file
fhand = open(file_name, "rb")
# pdfreader is readable variable object that will be parsed                                    
pdfreader = PyPDF2.PdfFileReader(fhand)

# Number of pages will allows us to parse through all pages
num_pages = pdfreader.numPages
count = 0
text = ""

# While loop will read through each page
while count < num_pages:
    pageObj = pdfreader.getPage(count)
    count += 1
    text += pageObj.extractText()

# PyPDF2 cannot read scanned files, so by using if condition we check if above library return words.
if text != "":
    text = text
# else we convert scanned/image based PDF files into text by using OCR library textract.
else:
    text = textract.process(r'C:\Users\HP\Documents\PyCharm Projects\Marry.pdf', method="pdfminer", extension="pdf")

# The word_tokenize() function will break our text phrases into individual words.
tokens = word_tokenize(text)
# We'll create a new list that contains punctuation we wish to clean.
punctuations = ['(', ')', ';', ':', '[', ']', ',']
# We initialize stopwords variable, which is list of words like "The," "I," "and," that don't hold value as keywords.
stop_words = stopwords.words('english')
# We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and not word in string.punctuation]

print(text)

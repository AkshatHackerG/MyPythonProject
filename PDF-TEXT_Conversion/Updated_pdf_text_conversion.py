"""
    This Program is used to extract PDF file data into Text data and print output on terminal screen.
    Usage: Change the name of PDF file from which you want to extract data.
    Then in line 35, put your file address which is saved locally in your machine and save it.
    Then go to your destination folder then click R-Shift+R-Click and then select "OPEN POWERSHELL WINDOW HERE" and then run your python program & enjoy.
    Caution: It won't extract data from scanned images.
"""

import pdfminer
# To convert simple, text-based PDF file into readable text in python
import PyPDF2
# To convert non-readable, scanned pdf file into readable text in python
import textract

# opens a file
file_name = open('pdf_file_name.pdf', "rb")
# pdfreader is readable variable object that will be parsed
pdfreader = PyPDF2.PdfFileReader(file_name)

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

else:
    # file location
    text = textract.process(r'file-destination-path/gift.txt', method='pdfminer')

print(text)
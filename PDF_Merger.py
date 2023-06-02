import sys
from PyPDF4 import PdfFileMerger
#Create an instance of PdfFileMerger() class
merger = PdfFileMerger()
#Append files
for i in range(1,len(sys.argv)):
    merger.append(sys.argv[i])
#Write out the merged PDF file
merger.write("merged-file.pdf")
merger.close()
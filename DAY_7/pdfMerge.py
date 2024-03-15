# Day 7(11-03-2024)
# PDF merger

import PyPDF2

# No od pdf files
pdFiles = ["1.pdf", "2.pdf"]

# With the this we can merge the 
merger = PyPDF2.PdfMerger()

for filename in pdFiles:
    pdFile = open(filename,"rb")
    pdfReader = PyPDF2.PdfReader(pdFile)
    merger.append(pdfReader)

pdFile.close()

# write all the data to the given output
merger.write("mergerd.file")
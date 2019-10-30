from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk
from tkinter import filedialog
import ntpath
import os
import glob


output_pdf = PdfFileWriter()

# grab the location of the file path sent
def path_leaf(path):
    head, tail = ntpath.split(path)
    return head

# graphical file selection
def grab_file_path():
    # use dialog to select file
    file_dialog_window = tk.Tk()
    file_dialog_window.withdraw()  # hides the tk.TK() window
    # use dialog to select file
    grabbed_file_path = filedialog.askopenfilenames()
    return grabbed_file_path


# file to be reversed
filePaths = grab_file_path()

# open file and read
for filePath in filePaths:
    with open(filePath, 'rb') as readfile:
        input_pdf = PdfFileReader(readfile)

        # reverse order one page at time
        for page in reversed(input_pdf.pages):
            output_pdf.addPage(page)

    # graphical way to get where to select file starting at input file location
    dirOfFileToBeSaved = os.path.join(path_leaf(filePath), 'reverse' + os.path.basename(filePath)) 
    # write the file created
    with open(dirOfFileToBeSaved, "wb") as writefile:
        output_pdf.write(writefile)
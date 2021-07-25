import fitz

from os import listdir
from os.path import isfile, join
import os
import datetime

from dotenv import load_dotenv
load_dotenv()
mypath = os.getenv('MYFOLDER')

imagePath = 'image'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for book in onlyfiles:
    startTime_pdf2img = datetime.datetime.now()#Start time
    path = mypath +'/' +book
    # print(path)
    if book.lower().endswith('.pdf'):
        # fp = open(path, 'rb')
        # ebook = pypdf.PdfFileReader(fp)
        # print(ebook.getDocumentInfo())
        # print(ebook.getXmpMetadata())
        # # parser = PDFParser(fp)
        # # doc = PDFDocument(parser)

        # print(doc.info)  # The "Info" metadata
        pdf = fitz.open(path)
        print(pdf.metadata)
        page = pdf[0]
        rotate = int(0)
                 # The scaling factor for each size is 1.3, which will generate an image with a resolution increase of 2.6 for us.
                 # If there is no setting here, the default picture size is: 792X612, dpi=96
        zoom_x = 1.33333333 #(1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):#Determine whether the folder where the image is stored exists
             os.makedirs(imagePath) # If the image folder does not exist, create it

        pix.writePNG(imagePath+'/'+'images_%s.png'% book)#Write the picture into the specified folder

        endTime_pdf2img = datetime.datetime.now()#end time
        print('pdf2img time=',(endTime_pdf2img-startTime_pdf2img).seconds)

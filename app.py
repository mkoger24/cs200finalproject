from flask import Flask, render_template, request, send_file, redirect, abort
from reportlab.pdfgen.canvas import Canvas
from PyPDF2 import PdfMerger
from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import time


app = Flask(__name__, template_folder='templates', static_folder='css')

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")



@app.route('/', methods=['POST'])
def downloadFile ():
    # read from the form
    title = request.form["patternTitle"]
    needle = request.form["needleSize"]
    weight = request.form["yarnWeight"]
    width = request.form["stitchesPerInch"]
    height = request.form["rowsPerInch"]
    unit = request.form["unitMeasure"]

    # write to pdf the form attributes
    canvas = Canvas('templates/patternpdfs/output2.pdf', pagesize=(612.0, 792.0))
    canvas.setFont("Times-Roman", 18)
    canvas.drawString(72, 735, "Knitting Pattern: " + title)
    canvas.setFont("Times-Roman", 12)
    canvas.drawString(72, 710, "Needle Size: " + needle)
    canvas.drawString(72, 700, "Yarn Weight: " + weight)
    canvas.drawString(290, 710, "20 stitch x 20 row swatch should measure " + width + " x " + height + " " + unit)
   
    # wait for image to be downloaded
    time.sleep(.5)


    im = Image.open('/Users/maekoger/Downloads/output.png')
    canvas.drawImage('/Users/maekoger/Downloads/output.png', 72,490,width=468,height=200, mask='auto') 


    # image processing - next steps
    # def score(im, height, width):
    #     score = 0

    #     scoreList=[]

    #     for i in range(height):
    #         for j in range(width):
    #             list = im[i, j]
    #             if all(v == 0 for v in list):
    #                 score = score + 1
    #             else:
    #                 score = score - 1
    #     scoreList.append(score)
    #     return(scoreList)


    # im = plt.imread('/Users/maekoger/Downloads/output.png')
    # height, width, depth = im.shape
    # print(score(im, height, width))

    canvas.save()

    path = "./templates/patternpdfs/output2.pdf"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='localhost')
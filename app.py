from flask import Flask, render_template, request, send_file, redirect, abort
from reportlab.pdfgen.canvas import Canvas
from PyPDF2 import PdfMerger
from PIL import Image
import numpy as np
import time



def imageProcess(title):
    # open "/Users/maekoger/Downloads" + title + png
    return "processing image"


app = Flask(__name__, template_folder='templates', static_folder='css')

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

# @app.route('/', methods=['POST'])
# def input():
#     return render_template("input-info.php")


@app.route('/', methods=['POST'])
def downloadFile ():
    title = request.form["patternTitle"]
    needle = request.form["needleSize"]
    weight = request.form["yarnWeight"]
    width = request.form["stitchesPerInch"]
    height = request.form["rowsPerInch"]
    unit = request.form["unitMeasure"]
    # image = request.form["theCanvas"]

    # with open('templates/patternpdfs/output.pdf', 'w') as outputFile:
    #     outputFile.write(title)
    #     outputFile.write("\nNeedle Size: ")
    #     outputFile.write(needle)
    #     outputFile.write("\nYarn Weight: ")
    #     outputFile.write(weight)
    #     outputFile.write("\n")

    canvas = Canvas('templates/patternpdfs/output2.pdf', pagesize=(612.0, 792.0))
    canvas.setFont("Times-Roman", 18)
    canvas.drawString(72, 735, "Knitting Pattern: " + title)
    canvas.setFont("Times-Roman", 12)
    canvas.drawString(72, 710, "Needle Size: " + needle)
    canvas.drawString(72, 700, "Yarn Weight: " + weight)
    canvas.drawString(290, 710, "20 stitch x 20 row swatch should measure " + width + " x " + height + " " + unit)
    # canvas.drawString(72, 690, image)
    canvas.drawString(72, 60, imageProcess(title))
    # canvas.drawInlineImage("/Downloads/templates/patternpdfs/canvas-image.png", 72, 690)
    # pdf_merger = PdfMerger()
    time.sleep(1.2)

    im = Image.open('/Users/maekoger/Downloads/output.png')

    n = np.array(im)

    blacks = np.where((n[:, :, 0:3] == [0,0,0]).all(2))

    xcoords, ycoords = np.where((n[:, :, 0:3] == [0,0,0]).all(2))

    canvas.drawString(72, 489, xcoords)


    # pixels = list(im.getdata())
    # width, height = im.size
    # pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    # for x in pixels:
    #     rgb_im = im.convert('RGB')
    #     r, g, b = rgb_im.getpixel((1, 1))

    #     if (r==0) and (g==0) and (b==0):
    #         print(x)

    canvas.drawImage('/Users/maekoger/Downloads/output.png', 72,490,width=468,height=200, mask='auto') 




    canvas.save()

        


    path = "./templates/patternpdfs/output2.pdf"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='localhost')
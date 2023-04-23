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

    # canvas.drawInlineImage("/Downloads/templates/patternpdfs/canvas-image.png", 72, 690)
    # pdf_merger = PdfMerger()
    time.sleep(.5)

    im = Image.open('/Users/maekoger/Downloads/output.png')

    n = np.array(im)

    canvas.drawImage('/Users/maekoger/Downloads/output.png', 72,490,width=468,height=200, mask='auto') 


    #define the vertical filter
    vertical_filter = [[-1,-2,-1], [0,0,0], [1,2,1]]

    #define the horizontal filter
    horizontal_filter = [[-1,0,1], [-2,0,2], [-1,0,1]]

    #read in the pinwheel image
    img = plt.imread('/Users/maekoger/Downloads/output.png')

    #get the dimensions of the image
    n,m,d = img.shape

    #initialize the edges image
    edges_img = img.copy()

    line = 480

    #loop over all pixels in the image
    for row in range(3, n-2):
        for col in range(3, m-2):
            
            #create little local 3x3 box
            local_pixels = img[row-1:row+2, col-1:col+2, 0]
            
            #apply the vertical filter
            vertical_transformed_pixels = vertical_filter*local_pixels
            #remap the vertical score
            vertical_score = vertical_transformed_pixels.sum()/4
            
            #apply the horizontal filter
            horizontal_transformed_pixels = horizontal_filter*local_pixels
            #remap the horizontal score
            horizontal_score = horizontal_transformed_pixels.sum()/4
            
            #combine the horizontal and vertical scores into a total edge score
            edge_score = (vertical_score**2 + horizontal_score**2)**.5
            
            #insert this edge score into the edges image
            edges_img[row, col] = [edge_score]*4

            # print(horizontal_score)
            print(edge_score)

            # if line < 72:
            #     # canvas.showPage()
            #     # line = 735
            #     # canvas.drawString(72, line, "horizontal score: " + horizontal_score + "vertical score: " + vertical_score)
            #     # line = line - 10
            # else:
            #     canvas.drawString(72, line, horizontal_score )
            #     line = line - 10

    #remap the values in the 0-1 range in case they went out of bounds
    edges_img = edges_img/edges_img.max()


    # imageWithEdges = im.filter(ImageFilter.FIND_EDGES)

    # canvas.drawImage(imageWithEdges, 72,290,width=468,height=200, mask='auto')


    # image = cv2.imread("meter.jpg")
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # wide = cv2.Canny(blurred, 50, 200)
    # mid = cv2.Canny(blurred, 30, 150)
    # tight = cv2.Canny(blurred, 210, 250)

    # def auto_canny_edge_detection(image, sigma=0.33):
    #     md = np.median(image)
    #     lower_value = int(max(0, (1.0-sigma) * md))
    #     upper_value = int(min(255, (1.0+sigma) * md))
    #     return cv2.Canny(image, lower_value, upper_value)

    # auto_edge = auto_canny_edge_detection(blurred)
    # cv2.imwrite("auto.jpg", auto_edge)


    # blacks = np.where((n[:, :, 0:3] == [0,0,0]).all(2))
    # xcoords, ycoords = np.where((n[:, :, 0:3] == [0,0,0]).all(2))

    # canvas.drawString(72, 489, xcoords)


    # pixels = list(im.getdata())
    # width, height = im.size
    # pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    # shape = []
    # for x in pixels:
    #     rgb_im = im.convert('RGB')
    #     r, g, b = rgb_im.getpixel((1, 1))

    #     if (r==0) and (g==0) and (b==0):
    #         shape.append(x)

    # line = 480
    # for x in shape:
    #     # canvas.drawString(72, line, x)
    #     # line = line + 10
    #     print(x)


    # # pixels = list(im.getdata())
    # # width, height = im.size
    # # pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    # # for p in pixels:
    # #     if

    # pixelValues = list(im.getdata())
    # pixelValues = np.array(pixelValues).reshape((width, height, 3))
    # print (np.where(pixelValues.sum(axis=1)))
    # (array([3, 4, 5], dtype=int64),)
    # canvas.drawString(72,480,pixelValues)




    canvas.save()

        


    path = "./templates/patternpdfs/output2.pdf"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='localhost')
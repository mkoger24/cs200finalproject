# Knitting an Algorithm

Knitting a Picture: Algorithmically Generated Patterns from Drawing Inputs

## About Knitting an Algorithm

This algorithm can be used in the creation of knitting patterns based on drawn images from the user. These drawn images will be transformed into a chart knitting pattern before looping through the 'chart' to create a written pattern, which is the type of pattern that is used most by knitters. 

Knitting a Picture will be run as a web application using Flask, Python, JavaScript, CSS, and HTML. On load, the application will have two types of input fields for the user to customize their pattern; gauge information and the drawn image to be knitted with the pattern. 

In the gauge input field, the user will be instructed to knit a 20 row by 20 column swatch with their chosen yarn and needles. This information will be used to make sure the finished fabric measures the same as the drawn shape, to scale. There will also be a place for the user to input the weight of their yarn, as well as the size of their needles for reference upon sharing the pattern with others. In this space, there will also be a text box for the user to name their knitting pattern. This name will show at the top of the pattern.

Below the gauge input field, there will be a field where the user can draw the shape they wish to draw. There will be options to draw, erase, and undo above the input field. 

## To run the program, read the following instructions

Use the command ```pip install -r requirements.txt``` to install the correct packages for use in running this program within your virtual environment. To run the program, use the command ```python3 app.py``` or ```flask run```.

Note: in order to run this program, you will need to change the path for your downloads in lines 41-2 of app.py. To run this program more than once, you will need to delete output.png from your downloads folder before running it again.
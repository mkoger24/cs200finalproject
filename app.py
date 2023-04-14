from flask import Flask, render_template, request, send_file

app = Flask(__name__, template_folder='templates', static_folder='css')

@app.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def input():
    return render_template("input-info.php")


@app.route('/download', methods=['GET', 'POST'])
def downloadFile ():
    title = request.form["patternTitle"]
    needle = request.form["needleSize"]
    weight = request.form["yarnWeight"]
    request.form[downloadImage]
    with open('templates/patternpdfs/output.txt', 'w') as outputFile:
        outputFile.write(title)
        outputFile.write("\nNeedle Size: ")
        outputFile.write(needle)
        outputFile.write("\nYarn Weight: ")
        outputFile.write(weight)
        outputFile.write("\n")



    path = "./templates/patternpdfs/output.txt"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='localhost')
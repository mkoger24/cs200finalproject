from flask import Flask, render_template, request, send_file

app = Flask(__name__, template_folder='templates', static_folder='css')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "./templates/patternpdfs/bernasconi2007.pdf"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='localhost')
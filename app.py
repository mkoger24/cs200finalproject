from Flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='css')

@app.route('/', methods='GET')
def home():
    return render_template(home.html)

if __name__ == "__main__":
    app.run(debug=True, host='localhost')
from flask import Flask
from flask import render_template, request

app = Flask(__name__)

################################################################
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/wireless_protocols')
def index1():
    return render_template('wireless_protocols.html')


################################################################
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
app = Flask(__name__)
from markov import Markov

@app.route('/')
def index():
    return render_template('index.html', caption = "")

@app.route('/caption', methods=['POST'])
def submit():
    if request.method == 'POST':
        text = request.form['caption']
    else:
        text = ""
    try:
        markov = Markov(text)
    except:
        return render_template('index.html', caption = "Invalid input")
    text = markov.generate()
    if text == None:
        text = "Needs more input"
    return render_template('index.html', caption = text)
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

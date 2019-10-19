from flask import Flask, render_template, request
app = Flask(__name__)
from markov import Markov
from scraper import Scraper
@app.route('/')
def index():
    return render_template('index.html', caption = "")
@app.route('/instructions')
def instructions():
    return render_template('instructions.html', caption = "")
@app.route('/caption', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['caption']
        start = request.form['start']
        end = request.form['end']
    else:
        return render_template('index.html', caption = "Invalid input", label = "Error")
    scraper = Scraper(username, start, end)
    text = scraper.text
    try:
        markov = Markov(text)
    except:
        return render_template('index.html', caption= "Invalid input", label = "Error")
    text = markov.generate()
    if text == None:
        text = "Needs more input"
    return render_template('index.html', label = "Generated Caption:", caption = text)
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

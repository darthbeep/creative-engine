from flask import Flask, render_template, request
app = Flask(__name__)
from caption import caption

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', caption = "")
    username = request.form['username']
    start = request.form['start']
    end = request.form['end']
    text = caption(username, start, end)
    if text:
        return render_template('index.html', label = "Generated Caption:", caption = text)
    return render_template('index.html', caption= "Invalid input, please check if username is correct", label = "Error")
@app.route('/instructions')
def instructions():
    return render_template('instructions.html', caption = "")

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

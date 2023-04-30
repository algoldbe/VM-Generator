from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    gender = request.form['gender']
    return f"Hello, {name}! Your gender is {gender}."

if __name__ == '__main__':
    app.run(debug=True)

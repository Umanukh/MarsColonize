from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/<title>')
def index(title="Миссия Колонизация Марса"):
    return render_template('base.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
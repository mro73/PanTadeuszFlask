from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/book/<book>')
def book(book):
    return render_template(f"k{book}.html")
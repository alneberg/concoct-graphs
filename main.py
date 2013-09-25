import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/test_scatter')
def test_scatter():
    return render_template('test_scatter.html')

if __name__ == '__main__':
    app.run(debug=True)

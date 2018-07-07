# coding: utf-8
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World! こんにちは世界！'

@app.route("/")
def index():
    message = 'サンプル メッセージ'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()

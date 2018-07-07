# coding: utf-8
from os.path import join, relpath
from glob import glob
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World! こんにちは世界！'

@app.route("/")
def index():
    path = "./static"
    image_names = [relpath(x, path) for x in glob(join(path, '*.jpeg'))]
    # static内の.pngファイルがimage_namesに格納されます。
    my_list = []
    for image in image_names:
        dic = {}
        dic['name'] = 'Github'
        dic['image_name'] = 'static/' + image
        dic['link_url'] = 'https://github.com/infinith4'
        my_list.append(dic)

    message = 'サンプル メッセージ'
    return render_template('index.html', message=my_list)

if __name__ == '__main__':
    app.run()

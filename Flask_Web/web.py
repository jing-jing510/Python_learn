# auth ： xiaokou
# date ： 2023/7/4 16:58
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/show/info')
def index():
    # return 'index'
    return render_template('index.html')

@app.route('/get/news')
def news():
    # return 'index'
    return "render_template('index.html')"

if __name__ == '__main__':
    app.run()
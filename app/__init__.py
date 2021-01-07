from flask import Flask, render_template, request
from app.main import test_kakao


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')

@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        img_url = request.form['input_url']
        detect_result = test_kakao.detect_adult(img_url)
    return render_template('result.html',img_url = img_url, detect_result = detect_result)




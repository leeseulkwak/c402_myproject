from flask import Flask
import test

 # svm에 폴더안에 test파일이 있기 떄문에 import 실행시 이렇게 해야함.

app = Flask(__name__)
comparison_str=test.comparison.to_string()

@app.route('/')
def hello_pybo():
    return comparison_str
    # return 'Hello, Pybo22222'
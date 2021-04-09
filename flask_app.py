
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/login', methods=['GET'])
def api_filter():
    # query_parameters = request.args

    # code = query_parameters.get('code')

    #     # Using readlines()
    # file1 = open('codes.txt', 'r')
    # Lines = file1.readlines()

    # # Strips the newline character
    # for line in Lines:
    #     line = line.replace("\n","")
    #     if line == code:
    #         return str.lower(str(code==line))

    return 'congratulations)'

if __name__ == '__main__':
    app.run()

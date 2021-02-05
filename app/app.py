import sys, os
from flask import Flask
from flask import request
# from django.shortcuts import render
# from django.template import loader
from flask import render_template

app = Flask(__name__, template_folder='templates')

#route for home page
@app.route("/")
def index():
    # return "HELLO"
    # return render(request,
    #               'index.html'
    #               )

    return render_template(
        'hello.html')

        # title='Hello BG.',
        # body="Hello you in Flask"
    # )

# #route for name page
# @app.route("/hello")
# def hello_name():
#     name = request.args['name']

#     return "Hello " + name

# #route for name page
# @app.route("/template/hello")
# def hello_name_template():
#     name = request.args['name']

#     return render_template("hello_name.html",
#         name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=5000)
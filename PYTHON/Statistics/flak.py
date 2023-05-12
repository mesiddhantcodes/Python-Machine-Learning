from flask import Flask
from flask import request
app=Flask(__name__)
#app is the object of flask  class
# /  is used to show the path of the written function to the server

@app.route("/")
def hello_world():
    return "<h1>Hwllo,wolrd!</h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hwllo,wolrd 1!</h1>"
@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hwllo,wolrd 2!</h1>"
@app.route("/test")
def test():
    a=8+6
    return "this is my function {}".format(a)
#here @app is same as the decorator

@app.route("/test2/test2")
def test2():
    data=request.args.get('x')
    #here x is the key by which we givr input

    return '''this is a data input from my url {}'''.format(data)
# http://127.0.0.1:5000/test2/test2?x=sudhhnfhnsdf is the example of the taking input with url


if __name__=="__main__":
    app.run(host="0.0.0.0")

from flask import Flask
application=Flask(__name__)
@application.route('/')
def hello_world():
    return 'Hi Flask, this is Sai and finally I did it'

if __name__=="__main__":
   application.run(debug=True)

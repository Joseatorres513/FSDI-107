from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
        return "Hello from flask"

@app.get("/test")
def text():
        return "Hello from the test page"

@app.get("/about")
def about():
        return "Jose Torres"

# create an endpoint that says hello using a variable instead of using a string

@app.get("/hello")
def hello():
        message = {"message":"Hey!"}
        return json.dumps(message)


app.run(debug=True) #that when i save the code, the changes are applied to the server
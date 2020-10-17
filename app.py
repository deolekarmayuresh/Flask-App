from flask import Flask
app = Flask(__name__)

# Template
@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

# debugger mode
if (__name__) == "__main__":
    app.run(debug=True)




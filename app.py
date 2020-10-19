from flask import Flask, render_template
app = Flask(__name__)

# routes
@app.route('/')
def hello_world():
    return render_template("table.html")

@app.route('/about')
def about():
    return '<h1>About Me</h1>'


# debugger mode
if (__name__) == "__main__":
    app.run(debug=True)




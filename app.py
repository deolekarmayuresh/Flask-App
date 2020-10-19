from flask import Flask, render_template
import pandas as pd
import csv
app = Flask(__name__,template_folder='Template')

# routes
@app.route('/')
def show_tables():
    data = pd.read_csv('a.csv')
    return render_template("table.html")

@app.route('/about')
def about():
    return '<h1>About Me</h1>'


# debugger mode
if (__name__) == "__main__":
    app.run(debug=True)




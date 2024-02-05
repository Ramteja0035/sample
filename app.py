# app.py
from flask import Flask, render_template
import file
# file.py

def my_function():
    return "Hello, World!"


app = Flask(__name__)

@app.route('/')
def index():
    # Call the function from file.py
    output = file.my_function()
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)

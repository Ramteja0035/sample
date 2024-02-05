# app.py
from flask import Flask, render_template
import file
def my_function():
    return "Hello, World
# app.py
@app.route('/')
def index():
    # Call the function from file.py
    output = file.my_function()
    return render_template('index.html', output=output)

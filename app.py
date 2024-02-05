from flask import Flask, render_template
import file
def my_function():
    return "Hello, World
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/get_output', methods=['GET'])
def get_output():
    output = file.my_function()
    return jsonify(output=output)
if __name__ == '__main__':
    app.run(debug=True)

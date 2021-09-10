from flask import Flask, json, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('add_number.html')

@app.route('/add_number')
def add_number():
    a = request.args.get('a',0 , type=int)
    b = request.args.get('b',0 , type=int)
    return jsonify(result = a + b)


if __name__=="__main__":
    app.run(debug=True)

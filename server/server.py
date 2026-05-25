from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_col_names')
def get_col_names():
    response = jsonify({
        'all': util.get_full_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_price", methods =['POST'])
def predict_price():
    company = request.form['company']
    inches = float(request.form['inches'])
    screen = request.form['screenresolution']
    cpu = request.form['cpu']
    ram = float(request.form['ram'])
    memory = request.form['memory']
    gpu = request.form['memory']
    weight = float(request.form['weight'])
    
    response = jsonify({
        'estimated_price': util.estimated_price(company, inches, screen, cpu, ram,memory, gpu, weight)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("starting flask app.....")
    util.load_artifacts()
    app.run()
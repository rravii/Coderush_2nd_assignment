import csv, json
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/api', methods=['GET'])
def api():
    # convert balanced dataset to json then send

    with open('preprocessed_heart_disease.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = [ row for row in reader] 

    
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
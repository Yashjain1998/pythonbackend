from flask import Flask, request, jsonify
from health_plans import suggest_health_plans
from transformer import interpret_query
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/generate_health_plans": {"origins": "http://localhost:3000"}})

@app.route('/')
def hello():
    return 'Welcome to Health Monitoring App!'
    
@app.route('/generate_health_plans', methods=['POST'])
def generate_health_plans():
    data = request.json
    print(request)
    query = data.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    interpreted_query = interpret_query(query)
    health_plans = suggest_health_plans(interpreted_query)
    return jsonify({"health_plans": health_plans})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

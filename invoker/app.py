from flask import Flask, request, jsonify
import requests
from concurrent.futures import ThreadPoolExecutor
from cache import get_cache, set_cache

app = Flask(__name__)
GENERATOR_URL = 'http://generator-service:5000/generate'

def call_generator_service(model_name, viewer_id):
    response = requests.post(GENERATOR_URL, json={"model_name": model_name, "viewerid": viewer_id})
    return response.json()

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    viewerid = data['viewerid']
    model_name = data['model_name']

    # Check cache
    cached_result = get_cache(viewerid)
    if cached_result:
        return jsonify({"cached_result": cached_result})

    # Run cascade
    model_names = [f"{model_name}_{i}" for i in range(5)]
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(lambda name: call_generator_service(name, viewerid), model_names))

    # Merge results (example: just combine the results into a list)
    merged_result = {"results": results}

    # Cache the merged result
    set_cache(viewerid, str(merged_result))

    return jsonify(merged_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

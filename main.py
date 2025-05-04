from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_audit():
    data = request.get_json()
    brand_name = data.get('brand_name')
    instagram_handle = data.get('instagram_handle')

    if not brand_name or not instagram_handle:
        return jsonify({'error': 'Missing brand_name or instagram_handle'}), 400

    with open('submissions_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), brand_name, instagram_handle])

    return jsonify({'message': f'Audit request received for {brand_name} (@{instagram_handle})'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_audit():
    data = request.json
    brand_name = data.get('brand_name')
    instagram_handle = data.get('instagram_handle')

    # Placeholder audit generation logic
    audit = {
        "brand": brand_name,
        "handle": instagram_handle,
        "summary": f"This is a basic audit report for {instagram_handle}."
    }

    return jsonify(audit)

if __name__ == '__main__':
    app.run(debug=True)

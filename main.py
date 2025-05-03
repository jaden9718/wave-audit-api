from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/audit", methods=["POST"])
def generate_audit():
    data = request.get_json()
    brand = data.get("brand_name")
    handle = data.get("instagram_handle")

    # Basic success response (mock audit)
    return jsonify({
        "status": "success",
        "brand": brand,
        "handle": handle,
        "message": f"Audit generated for {brand} ({handle})"
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

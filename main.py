from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_audit():
    data = request.get_json()
    brand_name = data.get('brand_name')
    instagram_handle = data.get('instagram_handle')

    if not brand_name or not instagram_handle:
        return jsonify({'error': 'Missing fields'}), 400

    prompt = f"Give a premium visual brand audit for {brand_name} on Instagram (@{instagram_handle}). Include tone of voice, visual identity, content strategy, highlight use, CTA strength, growth tips, and a closing Essentials Plan offer."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )

    audit_text = response.choices[0].message["content"]
    return jsonify({'audit': audit_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

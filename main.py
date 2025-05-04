from flask import Flask, request, jsonify
import openai
import os
from openai import OpenAI
app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/generate', methods=['POST'])
def generate_audit():
    try:
        data = request.get_json()
        brand = data.get('brand_name', 'Unknown Brand')
        handle = data.get('instagram_handle', 'unknownhandle')

        prompt = f"Generate a high-level Instagram brand audit for {brand} (@{handle}). Focus on tone, visual identity, growth bottlenecks, and give 3 suggestions."

        print(f"Received request for: {brand} / {handle}")

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a branding expert that audits Instagram pages."},
        {"role": "user", "content": prompt}
    ]
)
        print("Generated audit:", result)

        return jsonify({"url": result})

    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

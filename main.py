from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
openai_api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/generate', methods=['POST'])
def generate_audit():
    try:
        data = request.get_json()
        brand = data.get('brand_name', 'Unknown')
        handle = data.get('instagram_handle', 'unknown')

        prompt = f"Generate a high-level Instagram audit for {brand} (Instagram: {handle}). Focus on branding, content strategy, visual consistency, CTA, and growth bottlenecks."

        print(f"Received request for: {brand} / {handle}")

        client = OpenAI(api_key=openai_api_key)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a branding expert who writes premium Instagram brand audits."},
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content
        print("Generated audit:", result)

        return jsonify({"url": result})

    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

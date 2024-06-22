from flask import Flask, request, abort, jsonify
from app import run
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/ai", methods=["POST"])
def handle_prompt():

    data = request.json

    if not data or "city" not in data or "timing" not in data:
        return (jsonify({"response": "Prompt not available", "success": False}), 400)

    city = data["city"]
    timing = data["timing"]

    print(city, timing)

    if city and timing:
        processed_text = run(city=city, timing=timing)
        return (
            jsonify({"response": processed_text, "success": True}),
            200,
        )  # 200 indicates successful processing
    else:
        # Handle missing prompt error
        return (jsonify({"response": None, "success": False}), 400)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

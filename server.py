from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotion_detector", methods=["GET"])
def emotion_detector_api():
    text_to_analyze = request.args.get('text_to_analyze', '').strip()

    result = emotion_detector(text_to_analyze)

    # Handle blank or invalid input
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    # Format and return proper result
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
"""
Flask app to serve emotion detection on web.
"""

from flask import Flask, request, render_template
from EmotionDetection.mock_emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def get_emotion():
    """
    Process the posted text and return formatted emotion analysis.
    """
    text_to_analyze = request.args.get("textToAnalyze", "").strip()
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return formatted

if __name__ == "__main__":
    app.run(debug=True)

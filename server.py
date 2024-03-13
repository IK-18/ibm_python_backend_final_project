'''Flask application server'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_route():
    '''
    Route to detect emotions
    '''
    text = request.args["textToAnalyze"]
    res = emotion_detector(text)
    result = "For the given statement, the system response is "
    emotions = list(res.keys())
    emotions = emotions[:-1]
    for k, v in res.items():
        if not v:
            return "Invalid text! Please try again!"
        if k in emotions:
            if emotions.index(k) == len(emotions) - 2:
                result += f"'{k}': {v} and "
            elif emotions.index(k) == len(emotions) - 1:
                result += f"'{k}': {v}. The dominant emotion is {res['dominant_emotion']}."
            else:
                result += f"'{k}': {v}, "
    return result

@app.route("/")
def render_index():
    '''
    Route to render index
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)

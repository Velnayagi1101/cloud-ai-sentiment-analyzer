from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]

        # Temporary result
        # Cloud AI API will be connected later
        if "good" in text.lower() or "happy" in text.lower():
            sentiment = "Positive 😊"
        elif "bad" in text.lower() or "sad" in text.lower():
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

    return render_template(
        "index.html",
        sentiment=sentiment,
        text=text
    )


if __name__ == "__main__":
    app.run(debug=True)

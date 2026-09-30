from flask import Flask, render_template, request
import os
from huggingface_hub import InferenceClient

app = Flask(__name__)

# Get API token from environment variable
HF_TOKEN = os.environ.get("HF_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)


@app.route("/", methods=["GET", "POST"])
def home():

    sentiment = None
    score = None
    text = ""

    if request.method == "POST":

        text = request.form["text"]

        try:
            result = client.text_classification(
                text,
                model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
            )

            best_result = max(result, key=lambda x: x["score"])

            sentiment = best_result["label"]
            score = round(best_result["score"] * 100, 2)

        except Exception as e:

            sentiment = "Error"
            score = None
            print(e)

    return render_template(
        "index.html",
        sentiment=sentiment,
        score=score,
        text=text
    )


if __name__ == "__main__":
    app.run(debug=True)

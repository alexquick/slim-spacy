import spacy
import flask
import os

from flask import Flask

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")


@app.route("/<text>")
def run(text):
    doc = nlp(text)
    return {
        "noun_phrases": [chunk.text for chunk in doc.noun_chunks],
        "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"],
        "ents": list(map(repr, doc.ents)),
    }


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)))

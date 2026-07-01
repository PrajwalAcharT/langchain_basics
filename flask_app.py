
from flask import Flask, request, render_template_string
from llm_core import ask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    question = ""
    answer   = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            answer = ask(question)

    html = open("flask_app.html").read()
    return render_template_string(html, question=question, answer=answer)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

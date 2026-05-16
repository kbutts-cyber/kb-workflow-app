from flask import Flask, render_template, request
import json
from pathlib import Path

app = Flask(__name__)

DATA_PATH = Path("data/workflows.json")


def load_workflows():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/", methods=["GET", "POST"])
def index():
    workflows = load_workflows()

    selected_issue = None
    workflow = None

    if request.method == "POST":
        selected_issue = request.form.get("issue_type")
        workflow = workflows.get(selected_issue)

    if request.method == "GET" and workflows:
        selected_issue = list(workflows.keys())[0]
        workflow = workflows[selected_issue]

    return render_template(
        "index.html",
        workflows=workflows,
        selected_issue=selected_issue,
        workflow=workflow
    )


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(debug=True)
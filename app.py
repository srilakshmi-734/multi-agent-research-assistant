from flask import Flask, render_template, request
from planner import planner_agent
from writer import writer_agent
from verifier import verifier_agent
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_query = request.form["question"]

        plan = planner_agent(user_query)
        answer = writer_agent(plan)
        verification = verifier_agent(answer, user_query)

        data = {
            "timestamp": str(datetime.now()),
            "user_query": user_query,
            "plan": plan,
            "answer": answer,
            "verification": verification
        }

        with open("outputs.json", "a") as f:
            json.dump(data, f)
            f.write("\n")

        return render_template("index.html",
                               query=user_query,
                               plan=plan,
                               answer=answer,
                               verification=verification)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
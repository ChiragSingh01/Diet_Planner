import os
from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv
from openai import OpenAI
import pdfkit

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1"
)

# Configure wkhtmltopdf path if needed
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')  # update if needed!

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    age = request.form.get("age")
    gender = request.form.get("gender")
    dietary = request.form.get("dietary")
    goal = request.form.get("goal")
    days = request.form.get("days")

    prompt = f"Create a healthy {days} {dietary} meal plan for a {age}-year-old {gender} with the goal: {goal}."

    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": "You are a helpful diet assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    raw_text = response.choices[0].message.content

    # Parse text to sections + items
    plan = []
    current_section = None

    for line in raw_text.splitlines():
        if line.strip().startswith("**") and line.strip().endswith("**"):
            section = line.strip("*").strip(":").strip()
            current_section = {"title": section, "items": []}
            plan.append(current_section)
        elif "-" in line and current_section:
            item = line.strip("-").strip()
            current_section["items"].append(item)

    return render_template("result.html", plan=plan)

@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    # Same parsing as above
    plan_data = request.form.get("plan_data")
    import json
    plan = json.loads(plan_data)

    rendered = render_template("pdf_template.html", plan=plan)
    pdf = pdfkit.from_string(rendered, False, configuration=PDFKIT_CONFIG)

    with open("diet_plan.pdf", "wb") as f:
        f.write(pdf)

    return send_file("diet_plan.pdf", as_attachment=True)

@app.route("/planner")
def planner():
    return render_template("planner.html")

if __name__ == "__main__":
    app.run(debug=True)

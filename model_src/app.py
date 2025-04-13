from flask import Flask, request, jsonify, render_template
from chains.case_report_chain import create_case_report_chain

app = Flask(__name__)

# In-memory storage for review submissions
reviews = []

# Stepwise questions for the case report process
QUESTIONS = [
    "What is the patient name?",
    "What is the patient age?",
    "What is the patient's primary complaint and its duration?",
    "What are the key clinical observations or vital signs?",
    "Please provide relevant patient history (conditions, allergies, medications)."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_question', methods=['POST'])
def get_question():
    data = request.get_json()
    step = data.get("step", 0)
    if step < len(QUESTIONS):
        return jsonify({"done": False, "question": QUESTIONS[step]})
    return jsonify({"done": True})

@app.route('/generate_report', methods=['POST'])
def generate_report():
    try:
        data = request.get_json()
        answers = data.get("answers", {})
        
        report_input = {
            "name": answers.get("name"),
            "age": answers.get("age"),
            "complaint_duration": answers.get("complaint_duration"),
            "key_findings_vitals": answers.get("key_findings_vitals"),
            "relevant_history": answers.get("relevant_history"),
        }
        print("Processing report generation...")
        chain = create_case_report_chain()
        report_html = chain.invoke(report_input)
        return jsonify({"success": True, "report": report_html})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# New endpoint: Display the review form
@app.route('/review_form', methods=['GET'])
def review_form():
    return render_template('review_form.html')

# New endpoint: Process form submission and store the review
@app.route('/submit_review', methods=['POST'])
def submit_review():
    review_name = request.form.get("name")
    review_content = request.form.get("review")
    # Store review in memory (for demo purposes; in production, use a database)
    reviews.append({"name": review_name, "review": review_content})
    return render_template("review_thanks.html", name=review_name)

if __name__ == '__main__':
    app.run(debug=True)

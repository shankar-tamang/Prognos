from flask import Flask, request, jsonify, render_template
from model_src.chains.case_report_chain import create_case_report_chain

app = Flask(__name__)

# Stepwise questions
QUESTIONS = [
    "What is the patient's name?",
    "What is the patient's age?",
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

        print("done")
        chain = create_case_report_chain()
        report_html = chain.invoke(report_input)

        return jsonify({"success": True, "report": report_html})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)

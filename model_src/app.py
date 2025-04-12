from flask import Flask, request, jsonify, render_template
from chains.case_report_chain import create_case_report_chain

app = Flask(__name__)

# Stepwise questions
QUESTIONS = [
    "What is the patient's primary complaint and its duration?",
    "What are the key clinical observations or vital signs?",
    "Please provide relevant patient history (conditions, allergies, medications)."
]


def generate_structured_html_report(answers):
    complaint = answers.get("complaint_duration", "Not specified")
    findings = answers.get("key_findings_vitals", "Not specified")
    history = answers.get("relevant_history", "Not specified")

    return f"""
<div class="space-y-4">
  <div class="text-xl font-bold text-blue-600">🩺 Preliminary Medical Report</div>
  <div class="text-sm text-yellow-800 bg-yellow-100 border-l-4 border-yellow-500 p-2 rounded">
    This is an AI-generated preliminary report. Please consult a licensed physician for final diagnosis and treatment.
  </div>

  <section>
    <h2 class="text-lg font-semibold text-gray-800">1. Patient Summary</h2>
    <ul class="list-disc pl-5 text-gray-700">
      <li><strong>Chief Complaint:</strong> {complaint}</li>
      <li><strong>Key Clinical Findings:</strong> {findings}</li>
      <li><strong>Relevant History:</strong> {history}</li>
    </ul>
  </section>

  <section>
    <h2 class="text-lg font-semibold text-gray-800">2. Rx – Potential Prescription Considerations</h2>
    <ul class="list-disc pl-5 text-gray-700">
      <li>Assess current RA medication regimen and check for interactions.</li>
      <li>Use acetaminophen cautiously; avoid NSAIDs initially.</li>
      <li>Ensure lactose-free medication due to intolerance.</li>
    </ul>
  </section>

  <section>
    <h2 class="text-lg font-semibold text-gray-800">3. Dx – Potential Differential Diagnoses</h2>
    <ul class="list-disc pl-5 text-gray-700">
      <li>RA-related headache</li>
      <li>Medication-induced headache</li>
      <li>Infection or dermatological condition</li>
    </ul>
  </section>

  <section>
    <h2 class="text-lg font-semibold text-gray-800">4. Tx – Potential Treatment Approaches</h2>
    <ul class="list-disc pl-5 text-gray-700">
      <li>Initial treatment with acetaminophen if suitable</li>
      <li>Further testing of scalp condition if needed</li>
      <li>Continue lactose intolerance management</li>
    </ul>
  </section>

  <section>
    <h2 class="text-lg font-semibold text-gray-800">5. Case Management Steps</h2>
    <ul class="list-disc pl-5 text-gray-700">
      <li>Obtain detailed history and perform full physical exam</li>
      <li>Conduct lab tests (CBC, CRP, ESR), imaging if necessary</li>
      <li>Refer to neurologist and dermatologist as needed</li>
    </ul>
  </section>

  <div class="text-sm text-gray-600 italic mt-4">
    ⚠️ Final responsibility lies with the attending physician. This report is only for preliminary guidance.
  </div>
</div>
"""


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

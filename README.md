# Medical Chat Assistant

A modern, responsive Flask-based web application that serves as a Medical Chat Assistant. This app allows users (e.g., doctors or medical staff) to interact via a chat interface to collect patient information and generate a structured medical report using an LLM chain. It also includes a review form where users can submit feedback.

---

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Review Form Integration](#review-form-integration)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Features

- **Chat-based Interaction:**
  - Stepwise questions to gather patient details.
  - Dynamic conversation with a responsive chat interface.
- **LLM-Based Report Generation:**
  - Generates a well-structured HTML report using custom Tailwind CSS styling.
  - PDF export functionality via `html2pdf.js`.
- **Responsive Design:**
  - Mobile-first design with a responsive navbar and chat UI.
  - Dark/light mode toggle for user preference.
- **Toast Notifications:**
  - In-app, brief notification messages (toasts) for user feedback.
- **Review Form:**
  - A separate review form page to collect user feedback.
  - Option to store reviews persistently (in-memory for demo or via database for production).
  - Alternatively, the review form can be replaced by a Google Form embed.

---

## Technology Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy (optional, for persistent storage)
- **Frontend:** HTML, Tailwind CSS, Vanilla JavaScript, Axios, html2pdf.js
- **LLM Integration:** (via a custom chain imported from `chains.case_report_chain`)
- **Icons:** Font Awesome

---

## Project Structure

```
medical-chat-app/
│
├── app.py                         # Main Flask application
├── requirements.txt               # Python dependencies
├── render.yaml                    # (Optional) Render deployment config
├── README.md                      # Project documentation
├── chains/
│   └── case_report_chain.py       # Module to generate case reports via LLM
├── templates/
│   ├── index.html                 # Main chat interface with navbar
│   ├── review_form.html           # Review form page (Google Form embed option available)
│   └── review_thanks.html         # Thank-you page after review submission
└── static/                        # Static files (if any)
```

*Note:* In this demo, reviews are stored in memory. For production, consider integrating a database (e.g., PostgreSQL with Flask-SQLAlchemy) for persistent storage.

---

## Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/medical-chat-assistant.git
   cd medical-chat-assistant
   ```

2. **Create a Virtual Environment and Activate It:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *Make sure your `requirements.txt` includes at least:*

   ```
   Flask==2.2.5
   gunicorn==21.2.0
   # Additional packages like Flask-SQLAlchemy if you add persistence, etc.
   ```

4. **Set Environment Variables (if needed):**

   For development, you can create a `.env` file or set environment variables directly. For example:

   ```bash
   export FLASK_ENV=development
   export DATABASE_URL=postgresql://user:password@localhost:5432/yourdbname
   ```

---

## Usage

1. **Run the Flask Application:**

   ```bash
   python app.py
   ```

2. **Open the App:**

   Visit `http://127.0.0.1:5000` in your browser. Use the chat interface to start a new patient file by typing "New case". Follow the guided steps to provide patient details. A structured report will be generated, and you'll have the option to download it as a PDF.

3. **Review Form:**

   Navigate to the review form by clicking the "Review Form" link in the navbar. Fill out the form to submit your feedback.

---

## API Endpoints

- **`/` (GET):**  
  Renders the main chat interface (`index.html`).

- **`/get_question` (POST):**  
  Receives the current step number and returns the next question in the chat process.

- **`/generate_report` (POST):**  
  Accepts a JSON payload with patient responses, calls the LLM chain to generate a report in HTML format, and returns the report.

- **`/review_form` (GET):**  
  Renders the review form page (`review_form.html`).

- **`/submit_review` (POST):**  
  Handles review form submissions, stores the review, and displays a thank-you page (`review_thanks.html`).

---

## Deployment

### Deploying on Render

1. **Prepare Your Repository:**  
   Ensure your repository has `app.py`, `requirements.txt`, and `render.yaml` in the root folder.

2. **render.yaml Example:**

   ```yaml
   services:
     - type: web
       name: medical-chat-assistant
       runtime: python
       buildCommand: ""
       startCommand: gunicorn model_src.app:app  # Adjust if app.py is in a subfolder
       envVars:
         - key: PYTHON_VERSION
           value: 3.10
         - key: PYTHONPATH
           value: model_src  # Only if your app is under a subfolder like model_src
   ```

3. **Push to GitHub:**  
   Render will deploy directly from your GitHub repository. Follow Render's documentation for connecting your repo.

4. **Environment Variables:**  
   Set any required environment variables (like `DATABASE_URL` if using a database) via Render's dashboard.

---

## Review Form Integration

You have two options for the review form:

1. **Custom Flask Form:**  
   The provided templates (`review_form.html` and `review_thanks.html`) let users submit a review that gets stored on the server (currently in memory).

2. **Google Form Embed:**  
   Alternatively, you can replace the custom form in `review_form.html` with an embedded Google Form (using an `<iframe>`) if you prefer Google’s response management.

---

## Future Improvements

- **Persistent Storage:**  
  Integrate a database (e.g., PostgreSQL with Flask-SQLAlchemy) for permanent review storage.

- **User Authentication:**  
  Add login functionality if the app is intended for use by authenticated medical staff only.

- **Advanced LLM Integration:**  
  Enhance the chain used for report generation by integrating additional checks, custom prompts, or fine‑tuning the model.

- **UI Enhancements:**  
  Add additional responsive tweaks, support for multiple languages, or further customization of the chat UI.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Happy coding!*


# Multi-Agent Research Assistant

A web-based Multi-Agent System built using Flask and Hugging Face models.

This project demonstrates how multiple AI agents can collaborate to solve a user query through structured task decomposition, content generation, and self-verification.

---

##  Project Overview

This system implements a **role-based multi-agent architecture** consisting of:

-  **Planner Agent** – Breaks the user query into structured sections
-  **Writer Agent** – Generates a detailed academic response
-  **Verifier Agent** – Evaluates completeness and correctness
-  **Self-Correction Loop** – Regenerates answer if verification fails

The application provides a simple web interface for interaction and logs all outputs for traceability.

---

## System Architecture

User Input  
⬇  
Planner Agent  
⬇  
Writer Agent  
⬇  
Verifier Agent  
⬇  
Final Output (with optional regeneration)

---

##  Technologies Used

- Python 3.11+
- Flask (Web Framework)
- Hugging Face `InferenceClient`
- HTML5
- CSS3
- JSON (Logging)

---

## Project Structure

multi_agent_web/
│
├── app.py
├── planner.py
├── writer.py
├── verifier.py
├── hf_model.py
├── requirements.txt
├── outputs.json
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

##  How It Works

1. User submits a question.
2. Planner agent decomposes it into structured sections.
3. Writer agent generates a detailed response.
4. Verifier agent evaluates the output.
5. If verification returns **FAIL**, the system regenerates the response.
6. All outputs are saved to `outputs.json`.

---

##  Installation & Setup

###  Clone the Repository

```bash
git clone <your-repository-link>
cd multi_agent_web

```

---

### Install Dependencies

Make sure you have **Python 3.10+** installed.

Install required libraries using:

```bash
pip install -r requirements.txt
```

---

###  Create `.env` File

Create a file named `.env` in the project root directory (same location as `app.py`).

Add your Hugging Face API token:

```
HF_API_TOKEN=your_huggingface_token_here
```

>  Important:
> - Do NOT add quotes around the token  
> - Do NOT add spaces around `=`  
> - Make sure `.env` is added to `.gitignore`  

Example `.gitignore`:

```
.env
```

---

###  Run the Application

Start the Flask development server:

```bash
python app.py
```

---

###  Open in Browser

Open your browser and go to:

```
http://127.0.0.1:5000
```

You should now see the **Multi-Agent Research Assistant** interface.

---

##  Example Test Questions

You can try the following questions:

- What is Machine Learning?
- Explain the concept of probability.
- Describe the role of mathematics in computer science.
- What is Artificial Intelligence?

---

##  Key Features

- Role-based multi-agent design
- Structured task decomposition
- Academic-style response generation
- Self-verification mechanism
- Regeneration on failure
- JSON logging for traceability
- Simple web-based interface

---

##  Future Improvements

- Add confidence scoring instead of PASS/FAIL
- Add multiple regeneration attempts
- Improve UI with modern styling
- Add evaluation metrics
- Deploy online (Render / Railway / Hugging Face Spaces)

---

##  Purpose of the Project

This project was developed to demonstrate:

- Multi-Agent System architecture
- Agent collaboration and communication
- Reliability via self-verification
- Integration of LLMs into web applications


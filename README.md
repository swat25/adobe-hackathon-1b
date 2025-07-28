# Adobe Hackathon 2025 – Round 1B  
### ✈️ Travel Planner: Connecting the Dots

This repository is the submission for **Round 1B** of the Adobe India Hackathon 2025.  
It implements an intelligent **travel assistant** that processes PDF guides and generates personalized, ranked summaries for a given persona and task.

---

## 🧠 Problem Statement

**Input:**  
- A list of travel guide PDFs  
- A persona (e.g. *Travel Planner*)  
- A job to be done (e.g. *Plan a 4-day trip for 10 college friends*)

**Goal:**  
- Extract meaningful sections  
- Rank them by relevance  
- Summarize intelligently  
- Return clean, structured output in JSON format

---

## 🧰 Tech Stack

- **Python 3.10**  
- `sentence-transformers` for semantic ranking  
- `transformers` for summarization (DistilBART)  
- `PyMuPDF (fitz)` for PDF reading  
- JSON for structured input/output  
- Clean modular design using virtual environments

---

## ⚙️ Setup Instructions

### ✅ Prerequisite: Python 3.10

Make sure you're using **Python 3.10**. You can check with:

```bash
python --version
````

> If you have multiple versions installed, use `python3.10` explicitly.

---

### 🧪 Step 1: Set up a Virtual Environment (Recommended)

```bash
# Navigate to your project directory
cd 1b

# Create a virtual environment named 'venv'
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

---

### 📦 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 📁 Step 3: Prepare Inputs

Ensure your folder looks like this:

```
1b/
├── input/
│   ├── *.pdf                  # All input travel guide PDFs
│   └── persona_job.json       # Contains persona & job-to-be-done
```

---

### ▶️ Step 4: Run the Project

```bash
python main.py
```

---

### 📤 Step 5: View Output

Your output will be generated at:

```
output/result.json
```

---

## ✨ Sample Output Structure

```json
{
  "metadata": {
    "persona": "Travel Planner",
    "job_to_be_done": "Plan a trip of 4 days...",
    "processing_timestamp": "2025-07-28T13:01:22..."
  },
  "extracted_sections": [ ... ],
  "subsection_analysis": [ ... ]
}
```

---

## 🤖 Key Features

* Smart semantic matching using `all-MiniLM-L6-v2`
* Lightweight, fast summarization using `distilbart-cnn-12-6`
* Handles deduplication and prioritization
* Clean separation of logic (extraction, ranking, summarization)

---


## 📝 License

This code is meant for demo and learning purposes as part of Adobe Hackathon.
Feel free to fork or reference with credits.


---


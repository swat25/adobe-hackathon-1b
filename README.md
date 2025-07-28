# Persona-Aware PDF Summarizer  
### Adobe India Hackathon 2025 – Round 1B

This project is a submission for **Round 1B** of the Adobe India Hackathon 2025.

It implements a smart document understanding system that takes in:
- a **persona** (e.g., Travel Planner),
- a **task or job to be done** (e.g., Plan a 4-day trip),
- and multiple **PDF documents** (e.g., travel guides, restaurant info, cultural tips)

...and returns a clean, ranked, and summarized JSON of the most relevant content.

---

## What This Project Does

Given a real-world problem framed as:
- a **persona**
- a **job to be done**
- a folder of **PDFs**

 It performs the following steps:

1. **Extracts text** from each PDF page  
2. **Ranks each section** based on how relevant it is to the given persona + task  
3. **Deduplicates** similar titles  
4. **Summarizes** top-ranked content using a fast, lightweight transformer model  
5. **Outputs** a structured JSON with extracted insights

---

## Folder Structure

```

1b/
├── input/
│   ├── \*.pdf                  # Input documents
│   └── persona\_job.json       # Contains persona and job/task
├── output/
│   └── result.json            # Final output saved here
├── main.py                    # Main runner script
├── extract\_text.py            # PDF text extractor
├── rank\_relevance.py          # Ranking engine (using sentence-transformers)
├── requirements.txt
└── README.md

````

---

## Example Use Case – Travel Planner

This project supports multiple test cases. Here's an example:

**Persona**: Travel Planner  
**Task**: Plan a 4-day trip for 10 college friends  
**Input PDFs**: Travel tips, hotel guides, cities, things to do in the South of France  
**Output**: Top 5 most relevant sections with summaries in `output/result.json`

You can inspect this example in the `input/` folder provided.

---

## Python Version

This project is tested on **Python 3.10**.  
Please make sure you're using Python 3.10+ for compatibility with packages like `sentence-transformers` and `transformers`.

---

## Local Setup

### Clone the repo

```bash
git clone https://github.com/swat25/adobe-hackathon-1b.git
cd adobe-hackathon-1b
````

### Step 1: Set up a Virtual Environment (Recommended)

#### Windows (with Python 3.10 specifically):

```bash
py -3.10 -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:

```bash
python3.10 -m venv venv
source venv/bin/activate
```

> Make sure Python 3.10 is installed on your system and added to PATH.

# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Prepare Inputs

Ensure your folder looks like this:

```
1b/
├── input/
│   ├── *.pdf                  # All input travel guide PDFs
│   └── persona_job.json       # Contains persona & job-to-be-done
```

---

### Step 4: Run the Project

```bash
python main.py
```

---

### Step 5: View Output

Your output will be generated at:

```
output/result.json
```

---

## Sample Output Structure

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


## Tech Stack

* **Python 3.10**
* `PyMuPDF (fitz)` – PDF parsing
* `sentence-transformers` – Semantic ranking (`all-MiniLM-L6-v2`)
* `transformers` – Summarization model (`sshleifer/distilbart-cnn-12-6`)
* `json` – Structured input/output
* Clean modular design using virtual environments
  
---

## Notes

* Only the top 5 deduplicated sections are included in the final output (based on ranking).
* The summarizer is lightweight and fast — ideal for hackathon use.

---









# Persona-Aware PDF Summarizer

**Adobe India Hackathon 2025 – Round 1B Submission**

This project is a solution to the Round 1B problem statement of the Adobe India Hackathon 2025.

The goal is to create a document intelligence system that reads a set of PDF files and intelligently selects and summarizes the most relevant content based on:

* A given **persona** (e.g., Travel Planner)
* A specific **task** or **job to be done** (e.g., Plan a trip)
* A set of **input PDFs**

The output is a clean, ranked, and summarized JSON response that surfaces only the most relevant insights.

---

## Folder Structure

```
1b/
├── input/
│   ├── *.pdf                  # Input documents
│   └── persona_job.json       # Contains persona and task
├── output/
│   └── result.json            # Final output saved here
├── main.py                    # Main runner script
├── extract_text.py            # PDF text extractor
├── rank_relevance.py          # Ranking engine (using sentence-transformers)
├── requirements.txt
└── README.md
```

---

##  Python Version

This project is tested with **Python 3.10**.
Please ensure you're using Python 3.10+ to avoid compatibility issues with


## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/swat25/adobe-hackathon-1b.git
cd adobe-hackathon-1b
```

### 2. Use Python 3.10 and Create a Virtual Environment

Make sure Python 3.10 is installed.

#### On Windows:

```bash
py -3.10 -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Place Input Files

Create or ensure this structure:

```
input/
├── *.pdf                  # Input documents
└── persona_job.json       # JSON file with persona and job
```

Example `persona_job.json` format:

```json
{
  "persona": { "role": "Travel Planner" },
  "job_to_be_done": { "task": "Plan a 4-day trip for a group of 10 college friends." },
  "documents": [
    { "filename": "Sample1.pdf", "title": "Sample1" },
    { "filename": "Sample2.pdf", "title": "Sample2" }
  ]
}
```

### 5. Run the Project

```bash
python main.py
```

### 6. View the Output

Check the file:

```
output/result.json
```

---

## Project Overview

The pipeline performs the following steps:

1. **Extracts** page-level text from all PDF files.
2. **Ranks** each section’s relevance using semantic similarity (with sentence-transformers).
3. **Deduplicates** similar section titles to avoid repetition.
4. **Summarizes** the top 5 sections using a transformer-based summarizer.
5. **Generates** a structured JSON output with metadata, ranked results, and summaries.

---

## Example Use Case

**Persona**: Travel Planner
**Task**: Plan a 4-day trip for a group of 10 college friends
**Input PDFs**: Travel guides, food/culture/history docs about the South of France
**Output**: A JSON file with the 5 most relevant and summarized section titles and pages

---

## Technologies Used

* Python 3.10
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (via `fitz`) for PDF text extraction
* [`sentence-transformers`](https://www.sbert.net/) for relevance ranking (`all-MiniLM-L6-v2`)
* [`transformers`](https://huggingface.co/transformers/) for summarization (`sshleifer/distilbart-cnn-12-6`)
* JSON for structured input/output

---

## Notes

* Only top 5 deduplicated, ranked sections are returned.
* The summarizer automatically avoids hallucinated content (e.g., replacing wrong words like “Mexico”).
* Output format is suitable for downstream automation or frontend use.

---



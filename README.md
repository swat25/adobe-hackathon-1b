
# Adobe Hackathon 2025 – Round 1B  
### ✈️ Travel Planner: Connecting the Dots

This repository contains the solution to **Round 1B** of Adobe India Hackathon 2025 – a travel planning assistant that intelligently scans PDFs and extracts the most relevant information based on a user persona and job-to-be-done.

The challenge involved reading multiple guide PDFs and producing a summarized, ranked output tailored to a specific user scenario.

---

## 🧠 Problem Statement

Given:
- A set of PDF documents (e.g., travel guides).
- A persona and a task (e.g., *Travel Planner* planning *4-day trip for college friends*).

The goal was to:
- Identify and rank the most relevant sections.
- Deduplicate content intelligently.
- Generate high-quality summaries.
- Return a clean, JSON-formatted output.

---

## 🗂 Project Structure

```

1b/
├── input/
│   ├── \*.pdf                  # Input travel guides
│   └── persona\_job.json       # Contains persona & job details
├── output/
│   └── result.json            # Final output with ranked summaries
├── extract\_text.py            # Extracts text from PDFs
├── rank\_relevance.py          # Embeds, scores & ranks sections
├── main.py                    # Orchestrates everything
├── requirements.txt           # Dependencies
└── README.md                  # You're here

````

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
````

### 2. Make sure your PDFs and `persona_job.json` are inside the `input/` folder.

### 3. Run the program

```bash
python main.py
```

### 4. Check output in:

```
output/result.json
```

---

## 📌 Output Example

```json
{
  "extracted_sections": [
    {
      "document": "South of France - Cities.pdf",
      "section_title": "Travel Tips",
      "importance_score": 0.52,
      "summary": "Key tips for making the most of your trip to the South of France..."
    },
    ...
  ]
}
```

---

## 🤖 Under the Hood

* Uses **MiniLM** (`all-MiniLM-L6-v2`) from SentenceTransformers for semantic similarity.
* Summarization powered by **DistilBART** (`sshleifer/distilbart-cnn-12-6`) for speed and conciseness.
* Cleans, deduplicates, and ranks content using cosine similarity.

---


## 📝 License

This repository is intended for educational/demo purposes for the Adobe Hackathon. Please do not use it for commercial applications without permission.

```

---


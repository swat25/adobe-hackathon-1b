import fitz  # PyMuPDF
import os

def extract_sections(documents):
    sections = []
    
    for doc in documents:
        filename = os.path.join("input", doc["filename"])
        try:
            reader = fitz.open(filename)
            for page_num, page in enumerate(reader, start=1):
                text = page.get_text().strip()
                lines = [line.strip() for line in text.split("\n") if line.strip()]
                for line in lines:
                    sections.append({
                        "document": doc["filename"],  # <- fixes document name
                        "page_number": page_num,
                        "section_title": line
                    })
        except Exception as e:
            print(f"[ERROR] Failed to extract from {filename}: {e}")
    return sections

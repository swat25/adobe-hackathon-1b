from sentence_transformers import SentenceTransformer, util

# Load the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_sections(sections, persona, job):
    # Combine persona and job as a single query
    query = f"{persona}: {job}"
    query_embedding = model.encode(query, convert_to_tensor=True)

    section_texts = [s["section_title"] for s in sections]
    section_embeddings = model.encode(section_texts, convert_to_tensor=True)

    # Compute cosine similarity
    scores = util.cos_sim(query_embedding, section_embeddings)[0].cpu().numpy()

    # Attach scores to each section
    for i, score in enumerate(scores):
        sections[i]["importance_score"] = float(score)
        sections[i]["importance_rank"] = i + 1  # optional: you can sort later if needed

    # Sort sections by score descending
    ranked = sorted(sections, key=lambda x: x["importance_score"], reverse=True)
    
    # Assign rank after sorting
    for idx, sec in enumerate(ranked):
        sec["importance_rank"] = idx + 1

    return ranked

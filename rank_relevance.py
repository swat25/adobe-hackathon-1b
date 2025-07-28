from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_sections(sections, persona, job):
    query = f"{persona}: {job}"
    query_embedding = model.encode(query, convert_to_tensor=True)

    section_texts = [s["section_title"] for s in sections]
    section_embeddings = model.encode(section_texts, convert_to_tensor=True)

    scores = util.cos_sim(query_embedding, section_embeddings)[0].cpu().numpy()

    for i, score in enumerate(scores):
        sections[i]["importance_score"] = float(score)
        sections[i]["importance_rank"] = i + 1  # optional: you can sort later if needed

    ranked = sorted(sections, key=lambda x: x["importance_score"], reverse=True)

    for idx, sec in enumerate(ranked):
        sec["importance_rank"] = idx + 1

    return ranked

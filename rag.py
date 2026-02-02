from sentence_transformers import SentenceTransformer
import faiss, os
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = []
for file in os.listdir("../data"):
    docs += open(f"../data/{file}", encoding="utf-8").read().split("\n")

embeddings = model.encode(docs)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def retrieve(question, k=3):
    q_embed = model.encode([question])
    _, idx = index.search(q_embed, k)
    return "\n".join([docs[i] for i in idx[0]])

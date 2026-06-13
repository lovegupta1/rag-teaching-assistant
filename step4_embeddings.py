import pandas as pd
from sentence_transformers import SentenceTransformer
import joblib
import os

# Data load karo
df = pd.read_csv("data/chunks.csv")
print(f"Total chunks: {len(df)}")

# Model load karo
print("Embedding model load ho raha hai...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Embeddings banao
print("Embeddings ban rahi hain...")
embeddings = model.encode(df["text"].tolist(), show_progress_bar=True)

# Joblib se save karo
joblib.dump(embeddings, "data/embeddings.joblib")
df.to_csv("data/chunks.csv", index=False)

print(f"Embeddings save ho gayi! Shape: {embeddings.shape}")
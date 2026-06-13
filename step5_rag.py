import pandas as pd
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from groq import Groq
from config import GROQ_API_KEY

# Data load karo
df = pd.read_csv("data/chunks.csv")
embeddings = joblib.load("data/embeddings.joblib")
model = SentenceTransformer("all-MiniLM-L6-v2")
client = Groq(api_key=GROQ_API_KEY)

def search_chunks(query, top_k=5):
    # Query ki embedding banao
    query_embedding = model.encode([query])
    
    # Cosine similarity calculate karo
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    
    # Top chunks dhundo
    top_indices = similarities.argsort()[-top_k:][::-1]
    top_chunks = df.iloc[top_indices]["text"].tolist()
    
    return top_chunks

def ask_question(question):
    # Top chunks dhundo
    chunks = search_chunks(question)
    context = "\n\n".join(chunks)
    
    # Groq ko bhejo
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Tu ek helpful teaching assistant hai. Neeche diye context ke basis pe question ka jawab de."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )
    
    return response.choices[0].message.content

# Test karo
print("RAG System Ready!")
question = "What is Python used for?"
print(f"\nQuestion: {question}")
print(f"\nAnswer: {ask_question(question)}")
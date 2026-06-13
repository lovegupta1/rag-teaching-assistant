from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from groq import Groq
from config import GROQ_API_KEY

app = Flask(__name__)

print("Loading data...")
df = pd.read_csv("data/chunks.csv")
embeddings = joblib.load("data/embeddings.joblib")
model = SentenceTransformer("all-MiniLM-L6-v2")
client = Groq(api_key=GROQ_API_KEY)
print("Done!")

def search_chunks(query, top_k=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    return df.iloc[top_indices]["text"].tolist()

def ask_question(question):
    chunks = search_chunks(question)
    context = "\n\n".join(chunks)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """You are a helpful teaching assistant. Follow these rules strictly:
1. Always respond in English only by default.
2. Only respond in Hinglish (Hindi+English mix) if the user explicitly writes in Hinglish or Hindi.
3. Never respond in Portuguese, Spanish, French, or any other language.
4. Keep answers clear and concise."""
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )
    return response.choices[0].message.content

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    answer = ask_question(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
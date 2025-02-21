from openai import OpenAI
from .vector_store import vector_store
import pandas as pd
import os
from dotenv import load_dotenv
import pathlib  # Add this to resolve paths dynamically

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_cocktails():
    base_path = pathlib.Path(__file__).parent.parent
    csv_path = base_path / "data" / "cocktails.csv"
    df = pd.read_csv(csv_path)
    cocktails = [{"name": row["name"], "ingredients": eval(row["ingredients"])} for _, row in df.iterrows()]
    vector_store.add_cocktails(cocktails)
    return cocktails

cocktails = load_cocktails()

def detect_preference(user_input):
    if "favorite" in user_input.lower() or "like" in user_input.lower():
        vector_store.add_user_preference(user_input)
        return True
    return False

def get_rag_response(query):
    retrieved = vector_store.search(query, k=5)
    context = "\n".join([f"{item['name']}: {', '.join(item['ingredients'])}" if 'name' in item else item['text'] for item in retrieved])
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content.strip()
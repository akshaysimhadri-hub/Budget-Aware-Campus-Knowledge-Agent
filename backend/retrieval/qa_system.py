import requests
import os
from dotenv import load_dotenv
from backend.retrieval.search import search_documents

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_answer(query):

    # Retrieve similar chunks
    results = search_documents(query)

    # Build context
    context = ""

    sources = []

    for res in results:

        source = res.get("source", "Unknown Source")
        page = res.get("page", "N/A")

        context += f"Source: {source} | Page: {page}\n"
        context += res["text"] + "\n\n"

        sources.append({
            "source": source,
            "page": page
        })

    # Prompt
    prompt = f"""
You are a helpful SASTRA Campus AI Assistant.

Answer the user's question ONLY using the provided context.

Rules:
- Give short and accurate answers.
- Use simple English.
- Use correct grammar and spelling.
- Mention the source at the end.
- Source format:
  [source.pdf, page X]

Context:
{context}

Question:
{query}

Answer:
"""

    try:

        # OpenRouter API call
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "tencent/hy3:free",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        # Convert response to JSON
        data = response.json()

        print("\n✅ DEBUG RESPONSE:\n", data)

        # Success
        if "choices" in data:

            answer = data["choices"][0]["message"]["content"]

            return {
                "answer": answer,
                "sources": sources
            }

        # API error
        else:

            return {
                "error": f"API Error: {data}"
            }

    except Exception as e:

        print("❌ ERROR:", str(e))

        return {
            "error": str(e)
        }


# Local testing
if __name__ == "__main__":

    query = input("Ask your question: ")

    result = generate_answer(query)

    print("\n✅ FINAL RESPONSE:\n")

    print(result)

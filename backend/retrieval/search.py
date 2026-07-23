from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


# Generate embeddings
def get_embedding(text):

    return model.encode([text]).tolist()


# Search documents using pgvector cosine similarity
def search_documents(query, top_k=5):

    print("🔄 Connecting to Supabase PostgreSQL...")

    query_embedding = get_embedding(query)[0]

    print("🔍 Searching documents...")

    sql = text("""
        SELECT
            id,
            content,
            source,
            page,
            embedding <=> CAST(:embedding AS vector) AS distance

        FROM documents

        ORDER BY distance

        LIMIT :top_k;
    """)

    with engine.connect() as conn:

        results = conn.execute(
            sql,
            {
                "embedding": str(query_embedding),
                "top_k": top_k
            }
        )

        rows = results.fetchall()

    final_results = []

    for row in rows:

        final_results.append({

            "text": row.content,

            "source": row.source,

            "page": row.page,

            "score": row.distance
        })

    return final_results


# Test search
if __name__ == "__main__":

    query = input("Enter your question: ")

    results = search_documents(query)

    print("\n✅ Top Results:\n")

    for i, res in enumerate(results):

        print(f"Result {i+1}")

        print("Score:", res["score"])

        print("Source:", res["source"])

        print("Page:", res["page"])

        print("Text:", res["text"][:300])

        print("-----")
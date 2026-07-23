from backend.ingestion.chunk_data import chunk_documents
from backend.retrieval.search import get_embedding

from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# PostgreSQL connection
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
conn = engine.connect()


def store_embeddings():

    print("🔄 Loading chunks...")
    chunks = chunk_documents()

    print("🔄 Connected to Supabase PostgreSQL")
    print("🔄 Generating embeddings...")

    for i, chunk in enumerate(chunks):

        try:
            # Generate embedding
            embedding = get_embedding(chunk["text"])[0]

            # Insert into PostgreSQL
            query = text("""
                INSERT INTO documents
                (content, source, page, embedding)

                VALUES
                (:content, :source, :page, :embedding)
            """)

            conn.execute(
                query,
                {
                    "content": chunk["text"],
                    "source": chunk["source"],
                    "page": chunk["page"],
                    "embedding": embedding
                }
            )

            conn.commit()

            print(f"✅ Stored chunk {i+1}/{len(chunks)}")

        except Exception as e:

            conn.rollback()

            print(f"❌ Error at chunk {i}: {e}")

    print(f"\n🎉 Stored {len(chunks)} embeddings successfully!")


# ENTRY POINT
if __name__ == "__main__":
    store_embeddings()
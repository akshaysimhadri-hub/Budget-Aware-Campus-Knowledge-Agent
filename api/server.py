from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend files
app.mount("/static", StaticFiles(directory="frontend"), name="static")


# Request schema
class Query(BaseModel):
    question: str


# ROOT ROUTE → OPEN FRONTEND UI
@app.get("/")
def home():
    return FileResponse("frontend/index.html")


# ASK ENDPOINT
@app.post("/ask")
def ask_question(query: Query):

    try:

        from backend.retrieval.qa_system import generate_answer

        result = generate_answer(query.question)

        return result

    except Exception as e:

        print("❌ ERROR:", str(e))

        return {
            "error": str(e)
        }
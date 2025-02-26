from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Enable CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any domain (change this to your frontend URL if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Sample quiz questions
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Earth", "Venus", "Jupiter"], "answer": "Mars"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Dickens", "Austen", "Hemingway"], "answer": "Shakespeare"},
    {"question": "What is 5 + 3?", "options": ["5", "8", "7", "10"], "answer": "8"},
]

@app.get("/quiz")
def get_question():
    """Returns a random quiz question."""
    return random.choice(questions)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Earth", "Venus", "Jupiter"], "answer": "Mars"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Dickens", "Austen", "Hemingway"], "answer": "Shakespeare"},
    {"question": "What is 5 + 3?", "options": ["5", "8", "7", "10"], "answer": "8"},
    {"question": "Which is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "HO"], "answer": "H2O"},
    {"question": "Which country is famous for the Great Wall?", "options": ["China", "India", "Japan", "Russia"], "answer": "China"},
    {"question": "How many continents are there on Earth?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Which gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "Who painted the Mona Lisa?", "options": ["Van Gogh", "Leonardo da Vinci", "Picasso", "Rembrandt"], "answer": "Leonardo da Vinci"},
]


@app.get("/all-questions")
def get_all_questions():
    """Returns all quiz questions in order."""
    return questions

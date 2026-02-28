from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
app = FastAPI()

# Defining the shape of the data we are expecting to recieve
class BookTitle(BaseModel):
    book_name: str


@app.get("/")
async def root():
    return {"message": "Book Recommender API is running!"}

# When POST request hits, FastAPI will parse the JSON body and handles a BookTitle as title
@app.post("/recommend")
def create_title(title: BookTitle):
    return {"book_name": title.book_name}

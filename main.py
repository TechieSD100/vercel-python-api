# main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from JSON file
import os

json_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(json_path) as f:
    marks_data = json.load(f)


@app.get("/api")
def get_marks(request: Request):
    names = request.query_params.getlist("name")
    result = [marks_data.get(name, None) for name in names]
    return JSONResponse(content={"marks": result})

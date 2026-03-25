from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field, computed_field
from typing import List, Optional,Annotated,Literal
import json


app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Idea Stress Tester API!"}

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field, computed_field
from typing import List, Optional,Annotated,Literal
import json
from pathlib import Path

app = FastAPI()

class User(BaseModel):
    First_Name: Annotated[str, Field(..., description="The user's first name")]
    Last_Name: Annotated[str, Field(..., description="The user's last name")]
    Email: Annotated[str, Field(..., description="The user's email address")]
    Password1: Annotated[str, Field(..., description="The user's password")]
    Password2: Annotated[str, Field(..., description="Confirmation of the user's password")]

    @computed_field
    @property
    def Id(self) -> str:
        Id = self.Email.split('@')[0] + '_' + self.Password2[:]
        return Id
    @computed_field
    @property
    def Name(self) -> str:
        Name = self.First_Name + ' ' + self.Last_Name
        return Name
    @computed_field
    @property
    def Is_Password_Match(self) -> bool:
        same = self.Password1 == self.Password2
        return same


def load_data():
    data_path = Path(__file__).parent.parent / 'data' / 'users.json'
    if data_path.exists():
        with open(data_path, 'r') as f:
            data=json.load(f)
            return data
    else:
        return []
    
@app.post("/signup")
def signup(user: User):
    name = user.Name
    email = user.Email
    if not user.Is_Password_Match:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    # Here you would typically save the user to a database
    return {"message": f"User {user.Name} signed up successfully with ID {user.Id}"}
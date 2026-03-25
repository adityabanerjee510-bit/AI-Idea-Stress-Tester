from pydantic import BaseModel, Field, computed_field
from typing import List, Optional,Annotated,Literal
import json

class IdeaRequest(BaseModel):
    idea: str = Field(..., description="Detailed description of the idea to be stress tested")
    stress_test_type: Optional[Literal['market', 'technical', 'financial', 'operational']] = Field(None, description="The type of stress test to perform")
    additional_info: Optional[str] = Field(None, description="Any additional information relevant to the stress test")
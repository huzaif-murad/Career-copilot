from pydantic import BaseModel
from typing import List
class resumeAnalysis(BaseModel):
    strengths:List[str]
    weaknesses:List[str]
    improvements:List[str]
    questions:List[str]
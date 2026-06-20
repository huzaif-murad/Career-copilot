from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_resume(resume_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """You are an expert resume reviewer.
                
                Answer in following format.
                Return only valid json.
                {
  "strengths": [
    "Strong Python skills"
  ],
  "weaknesses": [
    "No internship experience"
  ],
  "improvements": [
    "Add quantified achievements"
  ],
  "questions": [
    "Explain your Expense Tracker project"
  ]
} 
                """
            },
            {
                "role": "user",
                "content": f"""
                Summarize the following resume in 5 bullet points:

                {resume_text}
                """
            }
        ]
    )

    return response.choices[0].message.content
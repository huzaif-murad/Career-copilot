from fastapi import APIRouter,UploadFile,File,HTTPException
from app.services.pdf_extractor import extract_text_from_pdf
from app.services.llm_service import analyze_resume
from app.schemas.resume import resumeAnalysis

router=APIRouter()

@router.post("/analyze-resume", response_model=resumeAnalysis)
async def upload_resume(file:UploadFile = File(...)) :
   text=extract_text_from_pdf(file.file)
   if not text:
      raise HTTPException(status_code=400,detail="No text found in pdf.")
   result=analyze_resume(text)

   return result

